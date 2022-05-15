import scrapy, re
from scrapy import Request
from ..items import ReedProjectItem

class ReedSpiderSpider(scrapy.Spider):
    name = 'reed_spider'
    start_urls = ['https://www.reed.co.uk/jobs/software-developer-jobs-in-london/']

    def parse(self,response):
        job_urls = response.xpath("//article[contains(@class,'job-result')]/a/@href").extract()
        job_title = response.xpath("//h3[contains(@class,'title')]/a/@title").extract()
        job_salaries = response.xpath("//li[contains(@class,'salary')]/text()").extract()
        job_type = response.xpath("//li[contains(@class,'time')]/text()").extract()
        job_location = response.xpath("//li[contains(@class,'location')]/span/text()").extract()
        for url,title,salary,time,location in zip(job_urls,job_title,job_salaries,job_type,job_location):
            yield Request('https://reed.co.uk'+url, callback=self.parse_document,
                          meta={"title":title ,"salary":salary,"time":time,"location":location})
        for url in response.xpath("//div[contains(@class,'pages')]/a/@href").extract():
            yield Request('https://reed.co.uk'+url)
    def parse_document(self, response):
        item = ReedProjectItem()
        item["title"] = response.meta.get("title")
        item["id"] = re.findall("\/(\d\d\d\d\d\d\d\d)\?",response.url)[0]
        item["salary"] = response.meta.get("salary")
        item["type"] = response.meta.get("time")
        item["location"] = response.meta.get("location")
        item["skills"] = response.xpath("//li[contains(@class,'skill-name')]/text()").extract() or ""
        item["is_remote"] = True if response.xpath("//*[contains(@class,'remote')]") else False
        item["description"] = response.xpath("//*[contains(@itemprop,'description')]/p/text()").extract_first() or ""
        yield item





