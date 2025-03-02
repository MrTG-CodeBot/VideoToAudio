import os

class VideoToAudioConverter:
    def __init__(self):
        pass

    def convert_to_audio(self, vid_path: str, aud_path: str) -> tuple[str | None, bool, str | None]:
        if not os.path.exists(vid_path):
            return None, False, "Video file not found."

        try:
            from moviepy import VideoFileClip
            video = VideoFileClip(vid_path)
            video.audio.write_audiofile(aud_path)
            video.close()

            if os.path.exists(aud_path):
                return aud_path, True, None
            else:
                return None, False, "Failed to create audio file."

        except ImportError:
            print("Run this command pip3 install -U -r requirements.txt")
            return None
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
