#!/bin/sh

cd ~/files-extra/2videocorso/webscraping-bible-course-master/06_scrape_amazon_to_create_price_trackers
source ~/files-extra/2videocorso/webscraping-bible-course-master/venv/bin/activate
cd ./tracker
scrapy crawl tracker

