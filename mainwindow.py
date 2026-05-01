import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from filemanager import FileManager
from metadatamanager import MetadataManager

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.file_mgr = FileManager(self, self.ui)
        self.metadata_mgr = MetadataManager(self, self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("Pyratag")
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
