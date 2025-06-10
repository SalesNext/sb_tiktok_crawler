import json
from yt_dlp import YoutubeDL

def parse_video_list(channel_url):
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'skip_download': True,
        'dump_single_json': True
    }
    url_list = []
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(channel_url, download=False)
        for entry in info_dict.get('entries', []):
            url_list.append(entry.get('url'))
    
    return url_list
            


