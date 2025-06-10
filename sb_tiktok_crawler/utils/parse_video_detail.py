from yt_dlp import YoutubeDL
from typing import Dict


def parse_video_detail(video_url: str) -> Dict:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        
        video = Video(
            video_id=info.get("id"),
            video_track_id=info.get("track"),
            video_artist=info.get("artist"),
            video_duration = info.get("duration"),
            video_title=info.get("title"),
            video_description=info.get("description"),
            video_view_count=info.get("view_count"),
            video_like_count=info.get("like_count"),
            video_repost_count=info.get("repost_count"),
            video_comment_count = info.get("comment_count"),
            source_video_url = info.get("original_url"),
            video_thumbnail = info.get("thumbnail"),
            video_upload_date = info.get("upload_date"),
            video_resolution = info.get("resolution"),
            
            
        )

    return video
