from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
)

from src.ui.pages.session.components.session_container import SessionContainer

class SessionDefaultView (QWidget):

    session_form_view_request = Signal()
    activity_page_request = Signal()

    session_container : SessionContainer

    def __init__(self, activity_name: str, sessions: list[tuple[int,str]]) -> None:
        super().__init__()

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Page title
        title_label = QLabel(activity_name)
        title_label.setObjectName("activityTitleLabel")
        title_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        #sessions container
        self.session_container = SessionContainer(sessions)

        # Buttons row
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)

        add_button = QPushButton("Add New Session")
        add_button.setObjectName("addSessionButton")

        back_button = QPushButton("Back to Activities")
        back_button.setObjectName("backToActivitiesButton")

        for button in (add_button, back_button):
            button.setMinimumHeight(70)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed,
            )

        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(back_button)

        # Signals
        add_button.clicked.connect(
            self.session_form_view_request.emit
        )

        back_button.clicked.connect(
            self.activity_page_request.emit
        )

        # Layout hierarchy
        self.main_layout.addWidget(title_label)
        self.main_layout.addWidget(
            self.session_container,
            stretch=1,
        )
        self.main_layout.addLayout(buttons_layout)

        # Styling
        self.setStyleSheet("""
            QLabel#activityTitleLabel {
                color: #111111;
                font-size: 30px;
                font-weight: 700;
                background-color: transparent;
                padding: 4px 0;
            }

            QPushButton#addSessionButton,
            QPushButton#backToActivitiesButton {
                background-color: #f3f3f3;
                border: 1px solid #dddddd;
                border-radius: 8px;

                color: #111111;
                font-size: 17px;
                font-weight: 600;
            }

            QPushButton#addSessionButton:hover,
            QPushButton#backToActivitiesButton:hover {
                background-color: #e5e5e5;
            }

            QPushButton#addSessionButton:pressed,
            QPushButton#backToActivitiesButton:pressed {
                background-color: #d8d8d8;
            }
        """)
        
