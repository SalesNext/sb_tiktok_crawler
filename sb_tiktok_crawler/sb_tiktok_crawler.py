from collections.abc import Iterable
from salesnext_crawler.crawler import ScrapyCrawler
from salesnext_crawler.events import CrawlEvent, Event, SitemapEvent
from scrapy import Request
import pyarrow as pa
from sb_tiktok_crawler.parser.parse_channel_list import parse_channel_list


class SbTiktokCrawler(ScrapyCrawler):
    def __init__(self, daily: bool = False
                 ) -> None:
        self.daily = daily
    def start(self) -> Iterable[Event]: 
                
        yield CrawlEvent(
        request = Request(f'https://socialblade.com/tiktok'),
        metadata= None,
        callback= parse_channel_list,
    )
            
            
         

    