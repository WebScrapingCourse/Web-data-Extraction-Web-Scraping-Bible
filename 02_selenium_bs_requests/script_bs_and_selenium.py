from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome("./chromedriver")

def extractor(page):
    driver.get("http://quotes.toscrape.com/page/{0}/".format(page))
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    texts = iter(x.text for x in soup.find_all("span", {"class": "text",}))
    authors = iter(x.text for x in soup.find_all("small", {"class": "author",}))
    tags = iter(x.text for x in soup.find_all("a", {"class": "tag",}))
    return texts, authors, tags

def main():
    with open("output_using_selenium.csv", 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["texts","authors","tags"])
        for page_number in range(1,11):
            texts,authors,tags = extractor(page_number)
            for _ in range(10):
                writer.writerow([next(texts),next(authors),next(tags)])

if __name__ == "__main__":
    main()


