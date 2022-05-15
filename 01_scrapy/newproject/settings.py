# Scrapy settings for newproject project

BOT_NAME = 'newproject'

SPIDER_MODULES = ['newproject.spiders']
NEWSPIDER_MODULE = 'newproject.spiders'

LOG_LEVEL = 'INFO'

ROBOTSTXT_OBEY = True

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
   'newproject.middlewares.NewprojectDownloaderMiddleware': 543,
}

# Enable or disable extensions
EXTENSIONS = {
   'newproject.extensions.NewExtension': None,
}










