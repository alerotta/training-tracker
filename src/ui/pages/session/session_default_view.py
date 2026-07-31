from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel
)
from src.ui.pages.session.components.session_container import SessionContainer

class SessionDefaultView (QWidget):

    session_form_view_request = Signal()
    activity_page_request = Signal()
    session_container = SessionContainer

    def __init__(self, activity_name: str, sessions: list[tuple[int,str]]) -> None:
        super().__init__()

        self.main_layout = QVBoxLayout(self)

        title_label = QLabel(activity_name)
        self.session_container = SessionContainer(sessions)

        add_button = QPushButton("Add New Session")
        add_button.clicked.connect(
            self.session_form_view_request.emit
        )

        back_button =  QPushButton("Back To Activities")
        back_button.clicked.connect(
            self.activity_page_request.emit
        )

        self.main_layout.addWidget(title_label)
        self.main_layout.addWidget(self.session_container)
        self.main_layout.addWidget(add_button)
        self.main_layout.addWidget(back_button)
        
