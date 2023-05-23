import subprocess
import re
from os.path import exists
from code.time_parser import seconds_to_h_m_s
import json
from time import time

def cut_video(start: int, end: int, input_file: str, output_file: str) -> int:
    """Cut video from start to end and save it to output_file.
    
    Args:
        start (int): Start time in seconds.
        end (int): End time in seconds.
        input_file (str): Input file path.
        output_file (str): Output file path.
    
    Raises:
        Exception: If ffmpeg return code is not 0 or output_file does not exist.

    Returns:
        int: Time in seconds of the process.
    """


    start_time = time()
    
    start = seconds_to_h_m_s(start)
    end = seconds_to_h_m_s(end)

    command = ['ffmpeg', '-ss', start, '-to', end, '-i', input_file, '-c', 'copy', '-map', '0', output_file]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    end_time = time()

    if result.returncode == 0 and exists(output_file):
        total_time = end_time - start_time
        return round(total_time, 2)
    
    raise Exception(result.stderr.decode('utf-8'))


def get_video_duration(filename: str) -> int:
    """Get video duration in seconds.

    Args:
        filename (str): Video filename.

    Returns:
        int: Video duration in seconds.

    Raises:
        Exception: If the command execution fails or the duration is not found in the output.
    """

    command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", 
               "-of", "json", filename]

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    stdout, _ = process.communicate()

    if process.returncode != 0:
        raise Exception("FFprobe command failed with output.")

    duration = json.loads(stdout)["format"]["duration"]
    return int(float(duration))
