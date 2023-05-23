from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QSpinBox
from PySide6.QtGui import QIcon
from ui.main import Ui_Form
from code.time_parser import seconds_to_time_ui, time_ui_to_seconds
from code.file_dialog import get_video_file_path
from code.video_edit import cut_video, get_video_duration


def msg_box(text: str, title: str = "Message") -> None:
    """Show a message box.

    Args:
        text (str): Message text.
        title (str, optional): Message title. Defaults to "Message".
    """
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec()

class MainApp(QWidget, Ui_Form):

    def _reset_ui(self):
        self.bt_cut_video.setEnabled(True)
        self.bt_cut_video.setText("Cut Video")
        self.lb_video_path.setText("Video path: No Selected")

        self.sp_start_h.setValue(0)
        self.sp_start_m.setValue(0)
        self.sp_start_s.setValue(0)

        self.sp_end_h.setValue(0)
        self.sp_end_m.setValue(0)
        self.sp_end_s.setValue(0)

        self.atm_video_duration = None
        self.video_path = None

    def _start(self):
        self.setWindowTitle("Fast Cut Video")
        self.setFixedSize(270, 160)
        self.setWindowIcon(QIcon("./ui/ico.ico"))

    def _select_video(self):
        self.video_path = get_video_file_path()

        if not self.video_path:
            return
        
        video_path_formatted = "..." + self.video_path[-20:] if len(self.video_path) > 20 else self.video_path

        self.lb_video_path.setText(f"Video path: {video_path_formatted}")
        self.atm_video_duration = get_video_duration(self.video_path)
        seconds_to_time_ui(self.atm_video_duration, self.sp_end_h, self.sp_end_m, self.sp_end_s)
    

    def _cut_video(self):
        
        if not self.video_path:
            return msg_box("No video selected", "Error")
        
        start = time_ui_to_seconds(self.sp_start_h, self.sp_start_m, self.sp_start_s)
        end = time_ui_to_seconds(self.sp_end_h, self.sp_end_m, self.sp_end_s)

        if start >= end:
            return msg_box("Start time must be less than end time", "Error")
        
        if end > self.atm_video_duration:
            return msg_box("End time must be less than video duration", "Error")
        
        self.bt_cut_video.setEnabled(False)
        self.bt_cut_video.setText("Cutting...")

        
        out_ext = self.video_path.split(".")[-1]
        out_path = self.video_path.replace(f".{out_ext}", f"_cut.{out_ext}")

        try:
            time_cut = cut_video(start, end, self.video_path, out_path)
        except Exception as e:
            return msg_box(str(e), "Error")
        
        text_format = "Video cut successfull"
        text_format += f"\nTime cut: {time_cut} seconds"
        text_format += f"\nOutput path: {out_path}"
        msg_box(text_format, "Success")
        self._reset_ui()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._start()
        self._reset_ui()

        self.atm_video_duration = None
        self.video_path = None

        self.bt_select_video.clicked.connect(self._select_video)
        self.bt_cut_video.clicked.connect(self._cut_video)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
