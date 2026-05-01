from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
import common

class MetadataManager:

    ui:Ui_MainWindow
    content:QWidget
    click_handler:common.OnClickHandler

    def __init__(self, window:QMainWindow, ui:Ui_MainWindow):
        self.ui = ui
        self.content = self.ui.metadata_content
        # click handler
        self.click_handler = common.OnClickHandler()
        self.click_handler.setWindow(window)
        self.click_handler.setWidget(self.content)
        self.click_handler.setCallback(self.onClick)

    def onClick(self):
        pass
