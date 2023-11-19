from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLineEdit, QDialog, QApplication


class PromptDialog(QDialog):
    def __init__(self, parent: QDialog, callback, *callback_params):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(QRect(0, 0, 0, 0))
        self.setStyleSheet("background-color: #ffdc99; border: 1px solid #888;font-size: 24px;")

        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(0, 0, self.width(), self.height())
        self.text_input.returnPressed.connect(self.get_prompt)

        self.callback = callback
        self.callback_params = callback_params

    def moveEvent(self, event):
        screen_rect = QApplication.desktop().screenGeometry()
        self.setGeometry(QRect(
            int(screen_rect.x() + screen_rect.width() * 0.4),
            int(screen_rect.y() + screen_rect.height() * 0.8),
            int(screen_rect.width() * 0.2),
            26
        ))
        self.text_input.setGeometry(0, 0, self.width(), self.height())

    def get_prompt(self):
        self.close()
        self.callback(self.text_input.text(), *self.callback_params)
