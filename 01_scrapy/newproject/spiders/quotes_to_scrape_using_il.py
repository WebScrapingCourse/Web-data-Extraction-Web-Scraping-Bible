import scrapy
from newproject.items import NewprojectItem
from scrapy import Request
import re
from scrapy import loader

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape_using_il'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        ItemLoader = loader.ItemLoader(NewprojectItem_UsingProcessors(), response=response)
        for quote in response.xpath('//div[@class="quote"]'):
            ItemLoader.add_xpath('text', './span[@class="text"]/text()')
            ItemLoader.add_xpath('author', './/small[@class="author"]/text()')
            ItemLoader.add_xpath('tags', './/div[@class="tags"]/a[@class="tag"]/text()')
            yield ItemLoader.load_item()

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield Request(response.urljoin(next_page_url))

