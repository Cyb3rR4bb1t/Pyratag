from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap

TEST_CURRENT_PATH = '/home/cyb3rr4bb1t/Music/Artists/Dream Thing/Satisfactory Soundtrack'
#TEST_CURRENT_PATH = '/home/cyb3rr4bb1t/Projects/qt/stealify/test'
AUDIO_EXT = ('.mp3', '.flac', '.wav', '.ogg', '.m4a')

class OnClickHandler(QObject):

    widget:QWidget

    def setCallback(self, function):
        self.function = function

    def setWindow(self, window):
        window.installEventFilter(self)

    def setWidget(self, widget):
        self.widget = widget

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            global_pos = event.globalPosition().toPoint() if hasattr(event, "globalPosition") else event.globalPos()
            local = self.widget.mapFromGlobal(global_pos)
            if self.widget.rect().contains(local):
                if self.function:
                    self.function()
        return super().eventFilter(obj, event)

def defaultCoverPixmap():
    pixmap = QPixmap()
    pixmap.load(':/images/photo-scan.png')
    return pixmap

def clearMetadataForm(ui):
    cover = defaultCoverPixmap()
    ui.cover_front_view.setPixmap(cover)
    ui.cover_back_view.setPixmap(cover)
    ui.prop_title.setText('')
    ui.prop_artist.setText('')
    ui.prop_album.setText('')
    ui.prop_album_artist.setText('')
    ui.prop_genre.setText('')
    ui.prop_year.setText('')
    ui.prop_track_num.setText('')
    ui.prop_track_total.setText('')
    ui.prop_disk_num.setText('')
    ui.prop_disk_total.setText('')
