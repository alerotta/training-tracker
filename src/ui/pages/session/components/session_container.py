from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from src.ui.pages.session.components.session_widget import SessionWidget

class SessionContainer (QWidget):

    def __init__(self, sessions: list[tuple[int,str]]) -> None:
        super().__init__()

        self.main_layout = QVBoxLayout(self)

        for session in sessions:
            self.add_session(session)

    def add_session(self, session: tuple[int,str]) -> None:
        session_widget = SessionWidget(session)
        self.main_layout.addWidget(session_widget)

    def reload_sessions(self, sessions: list[tuple[int,str]]) -> None:

        while self.main_layout.count() > 0:
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


        for session in sessions:
            self.add_session(session)
