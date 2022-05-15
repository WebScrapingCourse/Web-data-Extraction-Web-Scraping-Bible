import requests
from bs4 import BeautifulSoup
import csv

def extractor(page):
    print("http://quotes.toscrape.com/page/{0}/".format(page))
    request = requests.get("http://quotes.toscrape.com/page/{0}/".format(page))
    soup = BeautifulSoup(request.content, 'html.parser')
    texts = iter(x.text for x in soup.find_all("span", {"class": "text",}))
    authors = iter(x.text for x in soup.find_all("small", {"class": "author",}))
    tags = iter(x.text for x in soup.find_all("a", {"class": "tag",}))
    return texts, authors, tags

def main():
    with open("output.csv", 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["texts","authors","tags"])
        for page_number in range(1,11):
            texts,authors,tags = extractor(page_number)
            for _ in range(10):
                writer.writerow([next(texts),next(authors),next(tags)])

if __name__ == "__main__":
    main()
