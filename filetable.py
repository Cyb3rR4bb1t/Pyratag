from PySide6.QtWidgets import QTableWidget#, QTableWidgetItem
from PySide6.QtGui import QDropEvent
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt

class FileTable(QTableWidget):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._drop_row = -1

    def dragMoveEvent(self, event):
        index = self.indexAt(event.position().toPoint())
        self._drop_row = index.row() if index.isValid() else self.rowCount()
        self.viewport().update()
        event.accept()

    def dragLeaveEvent(self, event):
        self._drop_row = -1
        self.viewport().update()

    def dropEvent(self, event: QDropEvent):
        self._drop_row = -1
        self.viewport().update()
        source_row = self.currentRow()
        target_row = self.indexAt(event.position().toPoint()).row()
        if target_row == -1:
            target_row = self.rowCount() - 1
        items = [self.takeItem(source_row, col) for col in range(self.columnCount())]
        self.removeRow(source_row)
        self.insertRow(target_row)
        for col, item in enumerate(items):
            self.setItem(target_row, col, item)
        self.selectRow(target_row)

    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     if self._drop_row == -1:
    #         return
    #     painter = QPainter(self.viewport())
    #     painter.setPen(QPen(QColor("#4a90d9"), 2))
    #     if self._drop_row < self.rowCount():
    #         y = self.rowViewportPosition(self._drop_row)
    #     else:
    #         y = self.rowViewportPosition(self.rowCount() - 1) + self.rowHeight(self.rowCount() - 1)
    #     painter.drawLine(0, y, self.viewport().width(), y)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self._drop_row == -1:
            return
        row = min(self._drop_row, self.rowCount() - 1)
        painter = QPainter(self.viewport())
        painter.setPen(QPen(QColor("#4a90d9"), 2))
        painter.setBrush(Qt.NoBrush)
        y = self.rowViewportPosition(row)
        h = self.rowHeight(row)
        painter.drawRect(0, y, self.viewport().width() - 1, h)
