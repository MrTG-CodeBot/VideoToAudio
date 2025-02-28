# vid_aud/vid_aud.py

import os
import subprocess
from moviepy.editor import VideoFileClip

class VideoToAudioConverter:
    def __init__(self):
        pass

    def convert_to_audio(self, vid_path: str, aud_path: str) -> tuple[str | None, bool, str | None]:
        if not os.path.exists(vid_path):
            return None, False, "Video file not found."

        try:
            video = VideoFileClip(vid_path)
            video.audio.write_audiofile(aud_path)
            video.close()

            if os.path.exists(aud_path):
                return aud_path, True, None
            else:
                return None, False, "Failed to create audio file."

        except ImportError:
            try:
                subprocess.run(['pip', 'install', 'moviepy'], check=True)
                return self.convert_to_audio(vid_path, aud_path)  # retry after install
            except subprocess.CalledProcessError as e:
                return None, False, f"Failed to install moviepy: {e}"
            except Exception as e:
                return None, False, f"Error during moviepy install: {e}"
        except Exception as e:
            return None, False, f"Error converting video to audio: {e}"

    def video_check(self, vid_path: str) -> bool:
        if vid_path.lower().endswith((".mp4", ".mkv")):
            return True
        return False

    def audio_check(self, aud_path: str) -> bool:
        if aud_path.lower().endswith((".mp3", ".m4a", ".wav")):
            return True
        return False
