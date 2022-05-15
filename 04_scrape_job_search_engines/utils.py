import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

def connect_to_page_with_selenium(url):
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url)
    content = driver.page_source
    return BeautifulSoup(content, "lxml")

def connect_to_page(url):
    request = requests.get(url)
    return BeautifulSoup(request.content, "lxml")

def extraction_from_listing_page(writer,soup):
    job_urls = [x.a.get("href") for x in soup.find_all("article", {"class": "job-result"})]
    job_titles = [x.a.get("title") for x in soup.find_all("h3", {"class": "title"})]
    job_salaries = [x.text for x in soup.find_all("li", {"class": "salary"})]
    job_types = [x.text for x in soup.find_all("li", {"class": "time"})]
    job_location = [x.span.text for x in soup.find_all("li", {"class": "location"})]
    for url, title, salary, type, location in zip(job_urls, job_titles, job_salaries, job_types, job_location):
        soup = connect_to_page("https://www.reed.co.uk/"+url)
        tag_description = soup.find("span", {"itemprop": "description"})
        description = tag_description.text if tag_description else ""
        skills = [x.text for x in soup.find_all("li", {"class": "skill-name"})]
        is_remote = True if soup.find("div", {"class": "remote"}) else False
        id = re.findall("\/(\d\d\d\d\d\d\d\d)\?",url)[0]
        writer.writerow([title, id, salary, type, location, skills, is_remote, description])

