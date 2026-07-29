from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)

class ActivityFormView (QWidget):

    activity_default_request = Signal()

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        test = QPushButton("back")
        test.clicked.connect(
            self.activity_default_request.emit
        )
        self.main_layout.addWidget(test)
