import os
from ui_form import Ui_MainWindow
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QComboBox, QListWidget
import common
from audiotags import AUDIO_TAGS_MAP

class MetadataManager:
    def __init__(self, window:QMainWindow, ui:Ui_MainWindow):
        self.ui: Ui_MainWindow = ui
        self.window: QMainWindow = window
        # connections
        ui = self.ui
        ui.current_dir_view.textChanged.connect(self.__update_filesystem_tag_detectors)
        ui.files.itemSelectionChanged.connect(self.__update_title_combo)
        self.ui.files.itemSelectionChanged.connect(self.__update_metadata_form)
        ui.detect_title_combo.setEditable(False)
        ui.detect_title_btn.pressed.connect(self.__detect_title)
        ui.detect_artist_btn.pressed.connect(self.__detect_artist)
        ui.detect_album_btn.pressed.connect(self.__detect_album)

    def update_selected_tags(self, tag_name, value_callback):
        filenames = self.ui.files.selectedItems()
        if len(filenames) == 1:
            filename = filenames[0].text()
            if not AUDIO_TAGS_MAP.contains(filename):
                raise f"Tags not found for filename {filename}"
            AUDIO_TAGS_MAP.set_tag(filename, tag_name, value_callback(filename), True)
        if len(filenames) > 1:
            reply = QMessageBox.question(self.window, "Yes", "Are you sure you want to update all entries?",)
            if reply == QMessageBox.StandardButton.Yes:
                for filenameItem in filenames:
                    filename = filenameItem.text()
                    if not AUDIO_TAGS_MAP.contains(filename):
                        raise f"Tags not found for filename {filename}"
                    AUDIO_TAGS_MAP.set_tag(filename, tag_name, value_callback(filename), False)
        self.__update_metadata_form()

    @Slot()
    def __detect_title(self):
        if self.ui.detect_filesystem_group.isChecked():
            self.update_selected_tags(
                tag_name = 'title',
                value_callback = lambda filename: filename.rsplit(".",1)[0]
            )

    @Slot()
    def __detect_artist(self):
        if self.ui.detect_filesystem_group.isChecked():
            self.update_selected_tags(
                tag_name = 'artist',
                value_callback = lambda _: self.ui.detect_artist_combo.currentText()
            )

    @Slot()
    def __detect_album(self):
        if self.ui.detect_filesystem_group.isChecked():
            self.update_selected_tags(
                tag_name = 'album',
                value_callback = lambda _: self.ui.detect_album_combo.currentText()
            )

    @Slot()
    def __update_metadata_form(self):
        items = self.ui.files.selectedItems()
        self.ui.files_selection_count.setText(f"{len(items)} of {self.ui.files.count()} selected")
        if not items:
            common.clearMetadataForm(self.ui)
            return None
        if len(items) == 1:
            tags = AUDIO_TAGS_MAP.get(items[0].text())
            if tags: tags.updateUI(self.ui)
            return None
        merged_tags = AUDIO_TAGS_MAP.merge([i.text() for i in items])
        if merged_tags:
            merged_tags.updateUI(self.ui)

    @Slot()
    def __update_title_combo(self):
        files: QListWidget = self.ui.files
        filepaths = files.selectedItems()
        title_combo: QComboBox = self.ui.detect_title_combo
        title_combo.clear()
        title_combo.setStyleSheet("")
        if len(filepaths) < 1:
            return
        if len(filepaths) == 1:
            title_combo.addItem(filepaths[0].text().rsplit(".",1)[0])
        else:
            title_combo.addItem(QIcon(":/icons/lock.svg"),"<keep>")
            title_combo.setStyleSheet("color: blue;")

    @Slot(str)
    def __update_filesystem_tag_detectors(self, text:str):
        music_dir: str = os.path.expanduser("~/Music/")
        dir_parts: list[str] = ['', *os.path.expanduser(text).replace(music_dir, "").split("/")]
        album_combo: QComboBox = self.ui.detect_album_combo
        artist_combo: QComboBox = self.ui.detect_artist_combo
        album_combo.clear()
        artist_combo.clear()
        if len(dir_parts) < 1:
            return
        album_combo.addItems(dir_parts)
        album_combo.setCurrentIndex(album_combo.count()-1)
        if len(dir_parts) < 2:
            return
        artist_combo.addItems(dir_parts)
        artist_combo.setCurrentIndex(artist_combo.count()-2)
