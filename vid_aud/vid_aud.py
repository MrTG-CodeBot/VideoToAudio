
import os
try:
    from moviepy import VideoFileClip
except ImportError:
    import subprocess
    subprocess.run(['pip','install','moviepy'])

class VideoToAudioConverter:
    def __init__(self):
        pass

    def convert_to_audio(self, vid_path: str, aud_path: str) -> str or None or bool:
        if not os.path.exists(vid_path):
            return None

        try:
            video = VideoFileClip(vid_path)
            video.audio.write_audiofile(aud_path)
            video.close()

            if os.path.exists(aud_path):
                return aud_path, True
            else:
                return False

        except Exception as e:
            print(f"Error in converting video to audio: {e}")
            return None

    def video_check(self, vid_path: str) -> bool:
        if vid_path.lower().endswith((".mp4", ".mkv")):
            return True
        return False

    def audio_check(self, aud_path: str) -> bool:
        if aud_path.lower().endswith((".mp3", ".m4a", ".wav")):
            return True
        return False
