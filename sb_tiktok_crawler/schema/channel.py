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
    
    