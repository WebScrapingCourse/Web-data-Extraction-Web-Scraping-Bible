from scrapy.exceptions import IgnoreRequest

class ReedProjectDownloaderMiddleware:

    def process_request(self, request, spider):
        if "?pageno=" in request.url:
            if int(request.url.split("?pageno=")[1]) > 10:
                raise IgnoreRequest(request.url)


