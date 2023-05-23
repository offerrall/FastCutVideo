from PySide6.QtWidgets import QFileDialog
import os

def get_video_file_path() -> str | None:
    """Open a file dialog to select a video file and save the last file path to a cache file.

    Returns:
        str | None: Video file path or None if no file is selected.
    """

    last_file_path = ""
    if os.path.isfile("cache.txt"):
        with open("cache.txt", "r") as file:
            last_file_path = file.read()

    file_dialog = QFileDialog()
    file_dialog.setDirectory(last_file_path)
    file_dialog.setNameFilter("Videos (*.mp4 *.avi *.mkv *.flv *.mov)")
    
    if file_dialog.exec_():
        file_path = file_dialog.selectedFiles()[0]
        with open("cache.txt", "w") as file:
            file.write(os.path.dirname(file_path))
        return file_path

