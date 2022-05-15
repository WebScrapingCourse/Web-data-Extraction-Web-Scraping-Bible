import requests
from bs4 import BeautifulSoup
import csv
import re

def extractor(page):
    request = requests.get("http://quotes.toscrape.com/page/{0}/".format(page))
    soup = BeautifulSoup(request.content, 'html.parser')
    texts = iter(x.text for x in soup.find_all("span", {"class": "text",}))
    authors = iter(re.findall("(\w+)",x.text)[-1] for x in soup.find_all("small", {"class": "author",}))
    tags = iter(x.text for x in soup.find_all("a", {"class": "tag",}))
    return texts, authors, tags

def main():
    with open("output.csv", 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["texts","authors","tags"])
        for page in range(1,11):
            texts,authors,tags = extractor(page)
            for i in range(10):
                writer.writerow([next(texts),next(authors),next(tags)])

if __name__ == "__main__":
    main()

