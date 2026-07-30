from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QLabel,
)

class SessionWidget(QPushButton):

    def __init__(self, session: tuple[int,str]) -> None:
        super().__init__()

        id , date = session

        self.main_layout = QHBoxLayout(self)

        id_label = QLabel(str(id))
        date_label = QLabel(date)

        self.main_layout.addWidget(id_label)
        self.main_layout.addWidget(date_label)