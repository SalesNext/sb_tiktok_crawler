from yt_dlp import YoutubeDL
from sb_tiktok_crawler.schema.channel import Channel
def parse_channel_detail(channel_url):    
  

    ydl_opts = {
        'playlist_items': '1',
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
       
        channel = Channel(
            channel_id = info.get("id"),
            channel_title = info.get("title"),
            source_channel_url = info.get("webpage_url"),
            channel_uploader_id = info.get("uploader_id"),
            channel_description = info.get("description"),
            channel_view_count = info.get("view_count"),
            channel_like_count = info.get("like_count"),
            channel_repost_count = info.get("repost_count"),
            channel_comment_count = info.get("comment_count"),
            channel_release_year = info.get("release_year"),
            channel_duration = info.get("duration"),    
        )
        
        return channel

    
