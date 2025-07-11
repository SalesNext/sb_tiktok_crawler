from collections.abc import Iterable
from salesnext_crawler.events import CrawlEvent, DataEvent, Event
from scrapy.http.response.html import HtmlResponse
from scrapy import Request
from sb_tiktok_crawler.utils.parse_channel_detail import parse_channel_detail
from sb_tiktok_crawler.utils.parse_video_list import parse_video_list
from sb_tiktok_crawler.utils.parse_video_detail import parse_video_detail
from sb_tiktok_crawler.schema.channel import Channel
def parse_video(
    event: CrawlEvent[None, Event, HtmlResponse],
    response: HtmlResponse,
) -> Iterable[Event]:
    
    channel = Channel(
    channel_name = response.xpath("//span[@class='truncate max-w-full']/text()").get(),
    channel_user_id = response.xpath("//span[@class='text-sm font-normal opacity-90']/text()").get(),
    channel_follower_count = response.xpath('//p[contains(text(), "subscribers")]/parent::div/p[2]/text()').get(),
    channel_created_on = response.xpath('//p[contains(text(), "Created On")]/parent::div/p[2]/text()').get(),
    channel_view_count = response.xpath('//p[contains(text(), "views")]/parent::div/p[2]/text()').get(),
    channel_video_count = response.xpath('//p[contains(text(), "videos")]/parent::div/p[2]/text()').get(),
    channel_rating_grade = response.xpath('//h4[text()="Grade"]/preceding-sibling::h2[1]/text()').get(),
    
    )
    channel_detail = parse_channel_detail(f"https://www.tiktok.com/{channel.channel_user_id}")
    full_data_channel = channel.model_copy(update=channel_detail.model_dump(exclude_unset=True))
    yield DataEvent("channel", full_data_channel)
    videos = parse_video_list(f"https://www.tiktok.com/{channel.channel_user_id}")
    for video in videos:
        video_detail = parse_video_detail(video)
        yield DataEvent("video", video_detail)
        