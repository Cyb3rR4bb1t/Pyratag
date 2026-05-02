import os
from ui_form import Ui_MainWindow
from PySide6.QtCore import QObject, Slot#, Signal
from PySide6.QtWidgets import QFileDialog, QMainWindow, QListWidget, QListWidgetItem
import common
from audiotags import AUDIO_TAGS_MAP

class FileManager(QObject):

    def __init__(self, window:QMainWindow, ui:Ui_MainWindow):
        self.window=window
        self.ui = ui
        self.ui.files.setStyleSheet("QListWidget::item { padding: 4px; }")
        # connections
        self.ui.current_dir_btn.clicked.connect(self.__select_directory)
        self.ui.select_all_check.clicked.connect(self.__toggle_files_selection)
        self.ui.files.itemSelectionChanged.connect(self.__toggle_select_all_checkbox)
        #self.ui.search_btn.clicked.connect(self.search)
        if common.TEST:
            self.__load_files(common.TEST_CURRENT_PATH)

    @Slot(bool)
    def __toggle_files_selection(self, value:bool):
        if value:
            self.ui.files.selectAll()
        else:
            self.ui.files.clearSelection()

    @Slot()
    def __toggle_select_all_checkbox(self):
        count = len(self.ui.files.selectedIndexes())
        total = self.ui.files.count()
        self.ui.select_all_check.setChecked(count==total)

    @Slot()
    def __select_directory(self):
        text = self.ui.current_dir_view.text()
        directory = QFileDialog.getExistingDirectory(
            parent=self.window,
            caption="Select Directory",
            dir=text if text else os.path.expanduser("~/Music")
        )
        self.__load_files(directory)

    def currentDir(self) -> str:
        return self.ui.current_dir_view.text()

    def __load_files(self, path):
        if not path:
            return None
        self.ui.current_dir_view.setText(path)
        table: QListWidget = self.ui.files
        table.clear()
        try:
            filenames = os.listdir(path)
            for f in sorted(filenames):
                if f.lower().endswith(common.AUDIO_EXT):
                    AUDIO_TAGS_MAP.add(f, self.currentDir()+'/'+f)
                    table.addItem(QListWidgetItem(f))
            self.ui.files_selection_count.setText(f"0 of {table.count()} selected")
        except Exception as e:
            print(f"Error loading directory: {e}")

    # def search(self):
    #     self.load_files(self.ui.current_dir_view.text())
