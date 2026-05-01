from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QWidget, QLineEdit
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

def updateCoverSide(cover_widget, value:bytes):
    if value:
        try:
            pixmap = QPixmap()
            pixmap.loadFromData(value)
            cover_widget.setPixmap(pixmap)
        except:
            cover_widget.setPixmap(defaultCoverPixmap())
    else:
        cover_widget.setPixmap(defaultCoverPixmap())

def clear_tag_edit(line_edit:QLineEdit):
    for action in line_edit.actions():
        line_edit.removeAction(action)
    line_edit.setText('')


def clearMetadataForm(ui):
    cover = defaultCoverPixmap()
    ui.tag_cover_front.setPixmap(cover)
    ui.tag_cover_back.setPixmap(cover)
    line_edit_list: list[QLineEdit] = [
        ui.tag_title,
        ui.tag_artist,
        ui.tag_album,
        ui.tag_album_artist,
        ui.tag_genre,
        ui.tag_year,
        ui.tag_track_num,
        ui.tag_track_total,
        ui.tag_disk_num,
        ui.tag_disk_total
    ]
    for line_edit in line_edit_list:
        clear_tag_edit(line_edit)
