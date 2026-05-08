from PySide6.QtWidgets import QLineEdit, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from ui_form import Ui_MainWindow
import common
from audio.tag import Tag
from audio.tags import Tags

class AudioTags:

    title: str
    artist: str
    album: str
    album_artist: str
    genre: str
    year: str
    track_num: int
    track_total: int
    disk_num: int
    disk_total: int
    cover_front: bytes
    cover_back: bytes

    # placeholder tag for batch edit
    UNIQUE_TAG = object()

    def __init__(self):
        self.title:str = None
        self.artist:str = None
        self.album:str = None
        self.album_artist:str = None
        self.genre:str = None
        self.year:str = None
        self.track_num:int = None
        self.track_total:int = None
        self.disk_num:int = None
        self.disk_total:int = None
        self.cover_front:bytes = None
        self.cover_back:bytes = None

    def pprint(self):
        for key, val in vars(self).items():
            if type(val)==str or type(val)==tuple or type(val)==int:
                print(key, val, type(val).__name__)
            elif isinstance(val, bytes):
                print(key, len(val), type(val).__name__)
            else:
                print(key, '<unknown>', type(val).__name__)

    def updateUI(self, ui: Ui_MainWindow):
        for key, val in self.__dict__.items():
            prop_type = type(self).__annotations__[key]
            if prop_type == bytes:
                label:QLabel = getattr(ui, f"tag_{key}")
                common.updateCoverSide(label, val)
            else: # prop_type in {str, int, None}:
                line_edit:QLineEdit = getattr(ui, f"tag_{key}")
                common.clear_tag_edit(line_edit)
                line_edit.setStyleSheet("")
                if val is AudioTags.UNIQUE_TAG:
                    line_edit.setReadOnly(True)
                    line_edit.setStyleSheet("color: blue;")
                    line_edit.setText("<keep>")
                    line_edit.addAction(QIcon(":/icons/lock.svg"), QLineEdit.LeadingPosition)
                else:
                    line_edit.setReadOnly(False)
                    line_edit.setText(str(val) if val else '')

    def load(self, filepath: str):
        tags = Tags(filepath)
        tag:Tag = tags.data[0]
        annotations = AudioTags.__annotations__
        for tag in tags.data:
            if tag.key in annotations:
                setattr(self, tag.key, tag.value)
            else:
                continue

class AudioTagsMap:

    ui: Ui_MainWindow

    def __init__(self):
        self.file_tag_map: dict[str, AudioTags] = {}

    def initialize(self, ui: Ui_MainWindow):
        self.ui = ui

    def add(self, filename: str, filepath: str):
        tags = AudioTags()
        tags.load(filepath)
        self.file_tag_map[filename] = tags

    def get(self, filename: str) -> AudioTags:
        return self.file_tag_map.get(filename)

    def contains(self, filename: str) -> bool:
        return self.file_tag_map.get(filename) is not None

    def update_ui_tag(self, tag, value):
        line_edit:QLineEdit = getattr(self.ui, f"tag_{tag}")
        if not line_edit:
            raise f"Invalid tag '{tag}'"
        line_edit.setText(f"{value}")

    def set_tag(self, filename: str, tag: str, value: any):
        items = self.ui.files.findItems(filename, Qt.MatchExactly)
        if not items:
            raise "item not found for filename {filename}"
        tags = self.file_tag_map[filename]
        if getattr(tags,tag,None) == value:
            return
        tag_type = AudioTags.__annotations__[tag]
        if value and type(value) != tag_type:
            raise f"value must be of type {tag_type.__name__}"
        items[0].setIcon(QIcon(":/icons/asterisk.svg"))
        setattr(tags, tag, value)


    def merge(self, filenames: list[str]):
        if not filenames:
            return None
        elif len(filenames) == 1:
            return self.file_tag_map.get(filenames[0])
        props:dict=None
        for filename in filenames:
            tags = self.file_tag_map.get(filename)
            if not props:
                props = tags.__dict__.copy()
            if tags:
                current_tags = tags.__dict__.items()
                # Note: we allow value can be none, because it means the field is empty and it
                # should be possible to edit, otherwise it would be marked as AudioTags.UNIQUE_TAG and impossible to edit
                props = {k: v for k, v in current_tags if props.get(k) == v or v is None}
        merged = AudioTags()
        merged_keys = merged.__dict__.keys()
        for key in merged_keys:
            val = props.get(key)
            if val is not None:
                setattr(merged, key, val)
            elif key in props:
                setattr(merged, key, '')
            else:
                setattr(merged, key, AudioTags.UNIQUE_TAG)
        return merged

AUDIO_TAGS_MAP = AudioTagsMap()
