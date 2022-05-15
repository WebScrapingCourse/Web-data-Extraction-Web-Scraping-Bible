import scrapy
from scrapy import Field
from itemloaders.processors import Compose, TakeFirst, Identity, MapCompose
import re

class NewprojectItem(scrapy.Item):
    author = Field()
    text = Field()
    tags = Field()

class NewprojectItem_UsingProcessors(scrapy.Item):
    author = Field(
        input_processor=MapCompose(lambda extracted: re.findall("(\w+)",extracted)[-1]),
        output_processor=TakeFirst()
    )
    text = Field()
    tags = Field()

