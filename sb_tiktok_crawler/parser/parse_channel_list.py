from collections.abc import Iterable

from salesnext_crawler.events import CrawlEvent, DataEvent, Event
from scrapy.http.response.html import HtmlResponse
from scrapy import Request
from sb_tiktok_crawler.parser.parse_video import parse_video

def parse_channel_list(
    event: CrawlEvent[None, Event, HtmlResponse],
    response: HtmlResponse,
) -> Iterable[Event]:
    
    
    urls = response.xpath("//a[@class='block']/@href").getall()
    urls = list(set(urls))
    for url in urls[:2]:
        yield CrawlEvent(
            request= Request(url=response.urljoin(url)),
            metadata= None,
            callback = parse_video,
        )