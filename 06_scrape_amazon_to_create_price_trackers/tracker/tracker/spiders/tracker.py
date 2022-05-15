import scrapy
from ..items import TrackerItem


class TrackerSpider(scrapy.Spider):
    name = 'tracker'
    allowed_domains = ['amazon.co.uk','groupon.co.uk']
    start_urls = [
        'https://www.amazon.co.uk/Lenovo-IdeaPad-Storage-Graphics-Windows/dp/B09M7NDGQK',
        'https://www.groupon.co.uk/deals/vinsetto-massage-office-chair-range?'
    ]

    def parse(self, response):
        item = TrackerItem()
        if "amazon" in response.url:
            item["name"] = response.xpath("//span[@id='productTitle']/text()").extract_first().split("(")[0].strip()
            item["price"] = response.xpath("//span[@class='a-price-whole']/text()").extract_first().strip()
            item["site"] = "amazon.co.uk"
            item["description"] = response.xpath("//span[@id='productTitle']/text()").extract_first().strip()
        elif "groupon" in response.url:
            item["name"] = response.xpath("//h1[@id='deal-title']/text()").extract_first().strip()
            item["price"] = response.xpath("//div[@class='price-discount-wrapper']/div/text()").extract_first().strip().replace("£","")
            item["site"] = "groupon.co.uk"
            item["description"] = response.xpath("//div[@id='highlights']/p/text()").extract_first().strip()
        yield item



