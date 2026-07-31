from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
)
from src.ui.pages.session.components.session_widget import SessionWidget

class SessionContainer (QWidget):

    def __init__(self, sessions: list[tuple[int,str]]) -> None:
        super().__init__()

        # Main container layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Internal scrollable widget
        self.scroll_content = QWidget()

        # Layout containing session widgets
        self.sessions_layout = QVBoxLayout(self.scroll_content)
        self.sessions_layout.setContentsMargins(10, 10, 10, 10)
        self.sessions_layout.setSpacing(8)
        self.sessions_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        # Complete hierarchy
        self.scroll_area.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll_area)

        for session in sessions:
            self.add_session(session)

    def add_session(self, session: tuple[int,str]) -> None:
        session_widget = SessionWidget(session)
        self.sessions_layout.addWidget(session_widget)

    def reload_sessions(self, sessions: list[tuple[int,str]]) -> None:

        self.clear_sessions()
        for session in sessions:
            self.add_session(session)

    def clear_sessions(self) -> None:

        while self.sessions_layout.count() > 0:
            item = self.sessions_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()