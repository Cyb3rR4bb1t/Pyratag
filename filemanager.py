import os
from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog, QMainWindow, QListWidgetItem
from PySide6.QtGui import QIcon
import common
from audiotags import AudioTags

class FileManager:

    ui:Ui_MainWindow
    window:QMainWindow
    files:dict = {}

    def __init__(self, window:QMainWindow, ui:Ui_MainWindow):
        self.window=window
        self.ui = ui
        # connections
        self.ui.current_dir_btn.clicked.connect(self.__select_directory)
        self.ui.select_all_check.clicked.connect(self.__toggle_files_selection)
        self.ui.files.itemSelectionChanged.connect(self.__toggle_select_all_checkbox)
        self.ui.files.itemSelectionChanged.connect(self.__selection_changed)
        #self.ui.search_btn.clicked.connect(self.search)
        self.__load_files(common.TEST_CURRENT_PATH)

    # slot
    def __toggle_files_selection(self, value:bool):
        if value:
            self.ui.files.selectAll()
        else:
            self.ui.files.clearSelection()

    # slot
    def __toggle_select_all_checkbox(self):
        count = len(self.ui.files.selectedIndexes())
        total = self.ui.files.count()
        self.ui.select_all_check.setChecked(count==total)

    # slot
    def __selection_changed(self):
        items = self.ui.files.selectedItems()
        self.ui.files_selection_count.setText(f"{len(items)} of {self.ui.files.count()} selected")
        if len(items) == 0:
            common.clearMetadataForm(self.ui)
            return None
        if len(items) == 1:
            tags = self.files.get(items[0].text())
            if tags: tags.updateUI(self.ui)
            return None
        equal_props:dict=None
        for item in items:
            tags = self.files[item.text()]
            if not equal_props:
                equal_props = tags.__dict__
            if tags:
                equal_props = {k: v for k, v in tags.__dict__.items() if equal_props.get(k) == v or v == None}
        ui_tags = AudioTags()
        ui_tags_keys = ui_tags.__dict__.keys()
        for key in ui_tags_keys:
            val = equal_props.get(key)
            if val != None:
                setattr(ui_tags, key, val)
            elif key in equal_props:
                setattr(ui_tags, key, '')
            else:
                setattr(ui_tags, key, '<preserve>')
        ui_tags.updateUI(self.ui)

    # slot
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
        self.ui.files.clear()
        try:
            filenames = os.listdir(path)
            for f in sorted(filenames):
                if f.lower().endswith(common.AUDIO_EXT):
                    filepath = self.currentDir()+'/'+f
                    tags = AudioTags()
                    tags.load(filepath)
                    self.files[f] = tags
                    item = QListWidgetItem(QIcon(":/icons/file-music.svg"),f)
                    self.ui.files.addItem(item)
            self.ui.files_selection_count.setText(f"0 of {self.ui.files.count()} selected")
        except Exception as e:
            print(f"Error loading directory: {e}")

    # def search(self):
    #     self.load_files(self.ui.current_dir_view.text())
