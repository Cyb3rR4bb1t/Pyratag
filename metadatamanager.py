import functools
import os
from PySide6.QtGui import QIntValidator
from ui_form import Ui_MainWindow
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QComboBox, QListWidget, QLineEdit
import common
from audiotags import AUDIO_TAGS_MAP, AudioTags

class MetadataManager:
    def __init__(self, window:QMainWindow, ui:Ui_MainWindow):
        self.ui: Ui_MainWindow = ui
        self.window: QMainWindow = window
        # connections
        self.ui.current_dir_view.textChanged.connect(self.__update_filesystem_tag_detectors)
        self.ui.files.itemSelectionChanged.connect(self.__update_title_combo)
        self.ui.files.itemSelectionChanged.connect(self.__update_metadata_form)
        self.ui.detect_title_combo.setEditable(False)
        self.ui.detect_title_btn.pressed.connect(self.__detect_title)
        self.ui.detect_artist_btn.pressed.connect(self.__detect_artist)
        self.ui.detect_album_btn.pressed.connect(self.__detect_album)
        self.ui.dir_convention_combo.currentIndexChanged.connect(
            lambda _: self.__update_filesystem_tag_detectors(self.ui.current_dir_view.text())
        )
        editable_tags = [
            "title",
            "artist",
            "album",
            "album_artist",
            "genre",
            "year",
            "track_num",
            "track_total",
            "disk_num",
            "disk_total"
        ]
        tags_annotations = AudioTags.__annotations__
        for tag in editable_tags:
            line_edit:QLineEdit = getattr(ui, f"tag_{tag}")
            if tags_annotations[tag] == int:
                line_edit.setValidator(QIntValidator())
            callback=functools.partial(self.__tag_edited_callback, tag)
            # this callback will only be called when user edits text
            line_edit.textEdited.connect(callback)

    def __tag_edited_callback(self, tag:str, text:str):
        selected_items = self.ui.files.selectedItems()
        tags_annotations = AudioTags.__annotations__
        for item in selected_items:
            tag_type = tags_annotations[tag]
            if tag_type not in [str, int, None]:
                raise
            AUDIO_TAGS_MAP.set_tag(item.text(), tag, tag_type(text) if text else None)
        self.__update_metadata_form()

    def update_selected_tags(self, tag_name, value_callback):
        filenames = self.ui.files.selectedItems()
        if len(filenames) == 1:
            filename = filenames[0].text()
            if not AUDIO_TAGS_MAP.contains(filename):
                raise f"Tags not found for filename {filename}"
            AUDIO_TAGS_MAP.set_tag(filename, tag_name, value_callback(filename))
        if len(filenames) > 1:
            reply = QMessageBox.question(self.window, "Yes", "Are you sure you want to update all entries?",)
            if reply == QMessageBox.StandardButton.Yes:
                for filenameItem in filenames:
                    filename = filenameItem.text()
                    if not AUDIO_TAGS_MAP.contains(filename):
                        raise f"Tags not found for filename {filename}"
                    AUDIO_TAGS_MAP.set_tag(filename, tag_name, value_callback(filename))
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
        convention_parts = self.ui.dir_convention_combo.currentText().split("/")
        artist_index=0
        album_index=0
        for i, part in enumerate(reversed(convention_parts)):
            if part == 'Artist': artist_index=i
            elif part == 'Album': album_index=i
        dir_parts: list[str] = ['', *os.path.expanduser(text).replace(music_dir, "").split("/")]
        album_combo: QComboBox = self.ui.detect_album_combo
        artist_combo: QComboBox = self.ui.detect_artist_combo
        album_combo.clear()
        artist_combo.clear()
        if len(dir_parts) < 1:
            return
        album_combo.addItems(dir_parts)
        album_combo_index = album_combo.count()-album_index
        album_combo.setCurrentIndex(album_combo_index if album_combo_index >=0 else 0)
        artist_combo.addItems(dir_parts)
        artist_combo_index = artist_combo.count()-artist_index
        artist_combo.setCurrentIndex(artist_combo_index if artist_combo_index >=0 else 0)
