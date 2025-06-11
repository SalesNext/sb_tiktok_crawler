from pydantic import BaseModel
from typing import Optional, List

class Channel(BaseModel):
    channel_name: Optional[str] = None
    channel_id : Optional[str] = None
    channel_user_id: Optional[str] = None
    channel_follower_count: Optional[str] = None
    channel_created_on: Optional[str] = None
    channel_view_count: Optional[str] = None
    channel_video_count: Optional[str] = None
    channel_rating_grade: Optional[str] = None
    channel_title: Optional[str] = None
    source_channel_url: Optional[str] = None
    channel_rating_grade: Optional[str] = None
    channel_uploader_id: Optional[str] = None
    channel_description: Optional[str] = None
    channel_like_count: Optional[int] = None
    channel_repost_count: Optional[int] = None
    channel_comment_count: Optional[int] = None
    channel_release_year: Optional[int] = None
    channel_duration: Optional[int] = None
   
    
    
    