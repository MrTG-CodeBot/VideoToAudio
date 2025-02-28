import io
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8', errors='backslashreplace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf8', errors='backslashreplace')

import os
from vid_aud.vid_aud import VideoToAudioConverter
import colorama

colorama.init()

RED = colorama.Fore.RED
RESET = colorama.Style.RESET_ALL

txt = f"""
{RED}│█████╗ ██╗    ██╗███████╗ █████╗ ██████╗ ███╗    ███╗██╗███╗    ██╗██╗  ██╗│{RESET}
{RED}│██════╝╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗    ██║╚██╗██╔╝│{RESET}
{RED}│█████╗  ╚████╔╝ ███████╗███████║██║  ██║██╔████╔██║██║██╔██╗    ██║ ╚███╔╝ │{RESET}
{RED}│═══██║    ╚██╔╝  ╚════██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║ ██╔██╗ │{RESET}
{RED}│█████║    ██║    ███████║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██╔╝ ██╗│{RESET}
{RED}│═════╝    ╚═╝    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝      ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝│{RESET}
{RED}│code by: https://github.com/MrTG-CodeBot                                    │{RESET}
"""

def type_text(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Add a newline at the end

if __name__ == "__main__":
    for line in txt.splitlines():
        type_text(line)

    c = VideoToAudioConverter()
    video_path = input("Enter the path of the video located: ")
    video_path = video_path.replace('"', "")

    if c.video_check(video_path):
        print("Example: C:\\path\\tofolder\\filename.mp3 (Make sure to include the full path and the extension eg: .mp3, .wav)")
        music_path = input("Enter the full path and filename for the saved audio (e.g., C:\\path\\to\\my_audio.mp3): ")
        music_path = music_path.replace('"', "")
        if c.audio_check(music_path):
            music_file, success, error_message = c.convert_to_audio(vid_path=video_path, aud_path=music_path)
            if success:
                print(f"Successfully converted to {music_file}")
            else:
                print(f"Conversion failed: {error_message}")
        else:
            print("You didn't add the correct extension of the audio file(.mp3, .m4a, or .wav)")
    else:
        print("You didn't add the correct extension of the video file(.mp4 or .mkv)")
