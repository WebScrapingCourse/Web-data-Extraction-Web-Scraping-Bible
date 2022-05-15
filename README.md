# Web-data-Extraction & Web-Scraping Bible

The course material for the course [Web-data-Extraction & Web-Scraping Bible](https://www.udemy.com/course/).

# Requirements

This repository requires Python 3.5+. (The script [snscrape_data-extraction.py]() requires Python 3.8+)

---

# Content

## 🛠 01. Scrapy Fundamentals

In the directory [01_scrapy](), you can find an easy scrapy-project example. This project was realized in order to explain how scrapy works. You can start the scraping of the website [Quotes to Scrape](http://quotes.toscrape.com/) by launching:

```
$scrapy crawl quotes_to_scrape [-o quotes_to_scrape.csv]
```

## 🛠 02. Selenium, BeautifulSoup and Requests

The directory [02_selenium_bs_requests]() contains two scripts (independent from each other) to scrape data from the website [Quotes to Scrape](http://quotes.toscrape.com/).

```
$python script_bs_and_requests.py
```

## 🛠 03. RegularExpressions fundamentals

The directory [03_re_alongside_bs]() contains the [script_bs&requests&re.py]() which is similar to [script_bs_and_requests.py]() but uses regex to clean some extracted values.


## 🛠 04. Project 1: scrape job-search-engines

The directory [04_scrape_job_search_engines]() contains a scrapy-project and some additional independent scripts to extract data from a job-search-engine.

## 🛠 05. Project 2: extract data from APIs

The project [05_tweets_data_extraction]() allows to extract tweets and write on a PostgreSQL database. In order to run the project, you should download the PostgreSQL-installer here https://www.postgresql.org/download/ and start the PostgreSQL server. Then you can create a database and a table where you want to write your data, by:

```
$python create_db.py
```

In one command you can extract the tweets you need and write them on the database:

```
$python tweepy_data-extractor.py
```

## 🛠 06. Project 3: scrape data for a price-tracker

In the directory [06_scrape_amazon_to_create_price_trackers](), you can find a script which scrapes data concerning items for sale and works as a price-tracker. The project provides to write the extracted data in a google-worksheet. In order to use this project you need to generate google credentials from  [Google Workspace for Developers](https://developers.google.com/), this is basically a json file that you have to move on a specific directory in your computer (read https://docs.gspread.org/en/latest/oauth2.html).
In one command you can scrape data from target-websites and update the google-worksheet:

```
$scrapy crawl tracker
```

## 🛠 98. SQL reminder

The directory [98_sql_reminder] contain stuff that I used to explain how sql queries work.

## 🛠 99. Web reminder

The directories [99_web_reminder_*] contain some example of HTML, CSS, JAVASCRIPTS files that I used to explain how HTML, CSS and JAVASCRIPT work.

## 🛠 100. Dockerize an app reminder

The directories [100_dockerize_an_application_reminder_*] contain stuff that I used to explain how docker works.


# License

The scripts and documentation in this project are released under the [MIT License](LICENSE).
