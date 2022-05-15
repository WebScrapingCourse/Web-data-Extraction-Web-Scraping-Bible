import scrapy
from newproject.items import NewprojectItem
from scrapy import Request
import re

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        item = NewprojectItem()
        for quote in response.xpath('//div[@class="quote"]'):
            item['text'] = quote.xpath('./span[@class="text"]/text()').extract_first()
            item['author'] = re.findall("(\w+)",quote.xpath('.//small[@class="author"]/text()').extract_first())[-1]
            item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract_first()
            yield item

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield Request(response.urljoin(next_page_url))

