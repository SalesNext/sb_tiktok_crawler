from pydantic import BaseModel
from typing import Optional, List

class Video(BaseModel):
    video_id: Optional[str] = None
    video_track_id: Optional[str] = None
    video_artist: Optional[str] = None
    video_duration: Optional[int] = None
    video_title: Optional[str] = None
    video_description: Optional[str] = None
    video_view_count: Optional[int] = None
    video_like_count: Optional[int] = None
    video_repost_count: Optional[int] = None
    video_comment_count: Optional[int] = None
    source_video_url: Optional[str] = None
    video_thumbnail: Optional[str] = None
    video_upload_date: Optional[str] = None
    video_resolution: Optional[str] = None
    video_channel_name: Optional[str] = None
  
    