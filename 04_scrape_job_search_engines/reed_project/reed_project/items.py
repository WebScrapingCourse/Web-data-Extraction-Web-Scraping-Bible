import scrapy

class ReedProjectItem(scrapy.Item):

    title = scrapy.Field()
    id = scrapy.Field()
    salary = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()
    skills = scrapy.Field()
    is_remote = scrapy.Field()
    description = scrapy.Field()

