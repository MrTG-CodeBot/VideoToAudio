import os
from vid_aud.vid_aud import VideoToAudioConverter

RED = "\033[91m"
RESET = "\033[0m"

txt = f"""
 {RED}│█████╗ ██╗   ██╗███████╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗  ██╗│{RESET}
 {RED}│██════╝╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║╚██╗██╔╝│{RESET}
 {RED}│█████╗  ╚████╔╝ ███████╗███████║██║  ██║██╔████╔██║██║██╔██╗ ██║ ╚███╔╝ │{RESET}
 {RED}│═══██║   ╚██╔╝  ╚════██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║ ██╔██╗ │{RESET}
 {RED}│█████║    ██║   ███████║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██╔╝ ██╗│{RESET}
 {RED}│═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝│{RESET}
 {RED}│code by: https://github.com/MrTG-CodeBot                                │{RESET}
"""

if __name__ == "__main__":
    print(txt)
    c = VideoToAudioConverter()
    video_path = input("Enter the path of the video located: ")
    video_path = video_path.replace('"', "")

    if c.video_check(video_path):
        print("Example: C:\\path\\tofolder\\filename.mp3 (Make sure to include the full path and the extension eg: .mp3, .wav)")
        music_path = input("Enter the full path and filename for the saved audio (e.g., C:\\path\\to\\my_audio.mp3): ")
        music_path = music_path.replace('"', "")
        if c.audio_check(music_path):
            music_file, success = c.convert_to_audio(vid_path=video_path,aud_path=music_path)
            if success:
                print(f"Successfully converted to {music_file}")
            else:
                print("Conversion failed")
        else:
            print("You didn't add the correct extension of the audio file(.mp3, or .wav)")
    else:
        print("You didn't add the correct extension of the video file(.mp4 or .mkv)")
