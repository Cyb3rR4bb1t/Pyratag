import os
from ui_form import Ui_MainWindow
from PySide6.QtCore import QObject, Slot#, Signal
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QFileDialog, QMainWindow, QTableWidget, QTableWidgetItem, QListWidgetItem
from PySide6.QtCore import Qt
#from PySide6.QtGui import QIcon
import common
from audiotags import AudioTagsMap

class FileManager(QObject):

    def __init__(self, window:QMainWindow, ui:Ui_MainWindow):
        self.window=window
        self.ui = ui
        self.container = AudioTagsMap()
        # connections
        self.ui.current_dir_btn.clicked.connect(self.__select_directory)
        self.ui.select_all_check.clicked.connect(self.__toggle_files_selection)
        self.ui.files.itemSelectionChanged.connect(self.__toggle_select_all_checkbox)
        self.ui.files.itemSelectionChanged.connect(self.__selection_changed)
        #self.ui.search_btn.clicked.connect(self.search)
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
    def __selection_changed(self):
        items = self.ui.files.selectedItems()
        self.ui.files_selection_count.setText(f"{len(items)} of {self.ui.files.count()} selected")
        if not items:
            common.clearMetadataForm(self.ui)
            return None
        if len(items) == 1:
            tags = self.container.get(items[0].text())
            if tags: tags.updateUI(self.ui)
            return None
        merged_tags = self.container.merge([i.text() for i in items])
        if merged_tags:
            merged_tags.updateUI(self.ui)

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
            # table.setColumnCount(2)
            # table.setHorizontalHeaderLabels(["Track","Files"])
            # table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
            # table.setDragDropMode(QTableWidget.InternalMove)
            # table.setDragDropOverwriteMode(False)
            i = 0
            for f in sorted(filenames):
                if f.lower().endswith(common.AUDIO_EXT):
                    self.container.add(f, self.currentDir()+'/'+f)
                    table.addItem(QListWidgetItem(f))
                    # row = table.rowCount()
                    # table.insertRow(row)
                    # item = QTableWidgetItem(f)
                    # i+=1
                    # numItem = QTableWidgetItem(f"{i}")
                    # numItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    # table.setItem(row, 0, numItem)
                    # table.setItem(row, 1, item)#QIcon(":/icons/file-music.svg"),
            self.ui.files_selection_count.setText(f"0 of {table.count()} selected")
        except Exception as e:
            print(f"Error loading directory: {e}")

    # def search(self):
    #     self.load_files(self.ui.current_dir_view.text())
