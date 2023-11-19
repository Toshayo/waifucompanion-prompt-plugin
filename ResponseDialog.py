from PyQt5.QtCore import Qt, QRect, QPointF, QRectF
from PyQt5.QtGui import QColor, QPolygonF, QPainter
from PyQt5.QtWidgets import QLabel, QDialog

import EventManager


class ResponseDialog(QDialog):
    def __init__(self, parent: QDialog, message: str):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setStyleSheet('background-color: transparent; font-size: 20px;')

        self.lbl_message = QLabel(message, self)
        self.lbl_message.setWordWrap(True)
        self.lbl_message.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.update_pos()

        EventManager.INSTANCE.register_listener(
            EventManager.Events.COMPANION_WINDOW_MOVED, self.on_parent_move
        )

    def moveEvent(self, event):
        self.update_pos()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        polygon_points = [
            QPointF(0, self.height() * 0.2),
            QPointF(50, self.height() * 0.2),
            QPointF(50,  self.height() * 0.2 + 20)
        ]
        polygon = QPolygonF(polygon_points)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor('#ffdc99'))
        painter.drawPolygon(polygon)
        painter.drawRoundedRect(QRectF(50, 0, self.width() - 50, self.height()), 5, 5)

    def update_pos(self):
        self.setGeometry(QRect(
            int(self.parent().x() + self.parent().width() * 0.8),
            int(self.parent().y() + self.parent().height() * 0.4),
            400,
            110
        ))
        self.lbl_message.setGeometry(55, 5, self.width() - 60, self.height() - 10)

    def on_parent_move(self, _):
        self.update_pos()
