# 6ix4rmin9 Video to Audio Converter

A simple command-line tool to convert video files to audio formats.

![6ix4rmin9 Banner](https://raw.githubusercontent.com/MrTG-CodeBot/assets/main/banner.png)

## Features

- Convert MP4 and MKV video files to audio formats
- Support for multiple audio output formats (MP3, M4A, WAV)
- Simple command-line interface
- File format validation

## Requirements

- Python 3.6+
- MoviePy library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MrTG-CodeBot/6ix4rmin9.git
   cd 6ix4rmin9
   ```

2. Install the required dependencies:
   ```bash
   pip install moviepy
   ```

## Usage

Run the main script:
```bash
python main.py
```

Follow the prompts:
1. Enter the path to your video file (MP4 or MKV format)
2. Enter the desired output path for the audio file (including the extension: MP3, M4A, or WAV)

Example:
```
Enter the path of the video located: C:\Videos\myvideo.mp4
Enter the full path and filename for the saved audio: C:\Music\myaudio.mp3
```

## Project Structure

- `main.py` - The main script that handles user input and displays the banner
- `vid_aud.py` - Contains the `VideoToAudioConverter` class with conversion logic

## How It Works

The converter uses MoviePy to extract audio from video files. The process involves:

1. Validating the input video file format
2. Validating the output audio file format
3. Extracting the audio stream from the video
4. Saving the audio to the specified location

## Error Handling

The converter includes basic error handling for:
- Invalid file paths
- Unsupported file formats
- Conversion failures

## License

[MIT License](LICENSE)

## Author

Created by [MrTG-CodeBot](https://github.com/MrTG-CodeBot)

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
