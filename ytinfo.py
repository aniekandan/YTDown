def get_video_info(video) -> dict:
    try:
        # filter for progressive streams (contain both video and audio) and 
        # mp4 format
        streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        return {
            "streams": streams,
            "title": video.title,
            "duration": video.length
        }
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None