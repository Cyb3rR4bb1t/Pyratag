import sys
import os
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from filemanager import FileManager
from metadatamanager import MetadataManager
from audiotags import AUDIO_TAGS_MAP

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        AUDIO_TAGS_MAP.setUI(self.ui)
        self.ui.files.setIconSize(QSize(10, 10))
        self.metadata_mgr = MetadataManager(self, self.ui)
        self.file_mgr = FileManager(self, self.ui)

if __name__ == "__main__":
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.wayland.textinput=false"
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("Pyratag")
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
