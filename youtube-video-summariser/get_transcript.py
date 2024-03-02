from youtube_transcript_api import YouTubeTranscriptApi
import re


def get_transcript(video_link):
    try:
        regex_pattern = r"v=([^&]+)"
        video_id = re.search(regex_pattern, video_link).group(1)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ''
        for segment in transcript_list:
            transcript += segment['text'] + ' '
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

