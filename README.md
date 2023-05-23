# Fast Cut Video

Fast Cut Video is a simple and fast desktop application for cutting videos. This project was initially developed as a personal project to meet my own needs. I decided to share it with the community in case anyone finds this tool useful.

## Why It's Fast

Fast Cut Video utilizes the FFmpeg utility to perform the cutting operation. FFmpeg is known for its high speed in processing video and audio files. Instead of decoding and then re-encoding the video, which is time-consuming, Fast Cut Video simply copies the video and audio data, resulting in a much quicker cutting process. However, the exact speed can vary depending on your system's specifications.

## Dependencies

This project has minimal dependencies to keep it lightweight:

- Python: PySide6.
- System: FFmpeg.

## How to Install

1. Clone this repository or download the source code.
2. Ensure you have Python 3.7 or higher installed on your system.
3. Install the necessary Python dependency using pip:
    ```bash
    pip install PySide6
    ```
4. Ensure you have FFmpeg installed on your system. If not, you can download it from [here](https://ffmpeg.org/download.html).

## Running in a Local Environment

To run the application in a local environment, activate your Python virtual environment and execute the `main.py` script.

## How to Use

1. Run `main.py` to start the application.
2. Click on "Select Video" and select the video you want to cut.
3. Adjust the "Start" and "End" time spinners to decide the segment of the video you want to cut.
4. Click on "Cut Video". The cut video will be saved in the same directory as the original video with the "_cut" suffix in the file name.

This project is open source, so feel free to contribute and improve this tool. I hope you find Fast Cut Video useful!
