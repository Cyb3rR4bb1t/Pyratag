from mutagen import File
from PySide6.QtGui import QPixmap
from ui_form import Ui_MainWindow
import common

DEFAULT_AUDIO_TAGS = {
    'mp4': {
        'title':        [{'path': [0], 'tag': '©nam'}],
        'artist':       [{'path': [0], 'tag': '©ART'}],
        'album':        [{'path': [0], 'tag': '©alb'}],
        'album_artist': [{'path': [0], 'tag': 'aART'}],
        'genre':        [{'path': [0], 'tag': '©gen'}],
        'year':         [{'path': [0], 'tag': '©day'}],
        'track_number': [{'path': [0,0], 'tag': 'trkn'}],
        'track_total':  [{'path': [0,1], 'tag': 'trkn'}],
        'disk_number':  [{'path': [0,0], 'tag': 'disk'}],
        'disk_total':   [{'path': [0,1], 'tag': 'disk'}],
        'cover_front':  [{'path': [0], 'tag': 'covr'}],
        'cover_back':   [{'path': [], 'tag': ''}],
    },
    'm4a': {
        'title':        [{'path': [0], 'tag': '©nam'}],
        'artist':       [{'path': [0], 'tag': '©ART'}],
        'album':        [{'path': [0], 'tag': '©alb'}],
        'album_artist': [{'path': [0], 'tag': 'aART'}],
        'genre':        [{'path': [0], 'tag': '©gen'}],
        'year':         [{'path': [0], 'tag': '©day'}],
        'track_number': [{'path': [0,0], 'tag': 'trkn'}],
        'track_total':  [{'path': [0,1], 'tag': 'trkn'}],
        'disk_number':  [{'path': [0,0], 'tag': 'disk'}],
        'disk_total':   [{'path': [0,1], 'tag': 'disk'}],
        'cover_front':  [{'path': [0], 'tag': 'covr'}],
        'cover_back':   [{'path': [], 'tag': ''}],
    },
    'mp3': {
        'title':        [{'path': [0], 'tag': 'TIT2'}],
        'artist':       [{'path': [0], 'tag': 'TPE1'}],
        'album':        [{'path': [0], 'tag': 'TALB'}],
        'album_artist': [{'path': [0], 'tag': 'TPE2'}],
        'genre':        [{'path': [0], 'tag': 'TCON'}],
        'year':         [{'path': [0], 'tag': 'TDRC'}],
        'track_number': [{'path': [], 'tag': 'TRCK'}],
        'track_total':  [{'path': [], 'tag': 'TRCK'}],
        'disk_number':  [{'path': [], 'tag': 'TPOS'}],
        'disk_total':   [{'path': [], 'tag': 'TPOS'}],
        'cover_front':  [{'path': [0], 'tag': 'APIC:'}],
        'cover_back':   [{'path': [], 'tag': ''}],
    }
}

class AudioTags:
    def __init__(self):
        self.title:str = None
        self.artist:str = None
        self.album:str = None
        self.album_artist:str = None
        self.genre:str = None
        self.year:str = None
        self.track_number:int = None
        self.track_total:int = None
        self.disk_number:int = None
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

    def updateUI(self, ui:Ui_MainWindow):
        if self.cover_front:
            try:
                pixmap = QPixmap()
                pixmap.loadFromData(self.cover_front)
                ui.cover_front_view.setPixmap(pixmap)
            except:
                ui.cover_front_view.setPixmap(common.defaultCoverPixmap())
        else:
            ui.cover_front_view.setPixmap(common.defaultCoverPixmap())
        if self.cover_back:
            try:
                pixmap = QPixmap()
                pixmap.loadFromData(self.cover_back)
                ui.cover_back_view.setPixmap(pixmap)
            except:
                ui.cover_back_view.setPixmap(common.defaultCoverPixmap())
        else:
            ui.cover_back_view.setPixmap(common.defaultCoverPixmap())
        ui.prop_title.setText(self.title if self.title else '')
        ui.prop_artist.setText(self.artist if self.artist else '')
        ui.prop_album.setText(self.album if self.album else '')
        ui.prop_album_artist.setText(self.album_artist if self.album_artist else '')
        ui.prop_genre.setText(self.genre if self.genre else '')
        ui.prop_year.setText(self.year if self.year else '')
        ui.prop_track_num.setText(self.track_number if self.track_number else '')
        ui.prop_track_total.setText(self.track_total if self.track_total else '')
        ui.prop_disk_num.setText(self.disk_number if self.disk_number else '')
        ui.prop_disk_total.setText(self.disk_total if self.disk_total else '')

    def load(self, filepath: str):
        audio = File(filepath)
        if audio is None:
            raise ValueError(f"Unsupported file: {filepath}")
        extension = filepath.rsplit('.', 1)[-1].lower()
        audio_format = DEFAULT_AUDIO_TAGS.get(extension)
        if audio_format is None:
            raise ValueError(f"Unsupported format: {extension}")
        for uniform_key, entries in audio_format.items():
            for entry in entries:
                tag = entry['tag']
                path = entry['path']
                if not tag or tag not in audio:
                    continue
                value = audio[tag]
                if len(path)==0:
                    continue
                for path_part in path:
                    if value is None:
                        break
                    value = value[path_part]
                setattr(self, uniform_key, value)
                break
