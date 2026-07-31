from PySide6.QtCore import Signal , Qt
from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)

class SessionWidget(QPushButton):

    def __init__(self, session: tuple[int,str]) -> None:
        super().__init__()

        self.session_id, self.session_date = session

                # Button dimensions and cursor
        self.setMinimumHeight(70)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        # Internal layout
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(20, 10, 20, 10)
        self.main_layout.setSpacing(8)

        # Main session information
        date_label = QLabel(self.session_date)
        date_label.setObjectName("sessionDateLabel")

        # Secondary session information
        id_description_label = QLabel("Session ID:")
        id_description_label.setObjectName("sessionIdDescriptionLabel")

        id_label = QLabel(str(self.session_id))
        id_label.setObjectName("sessionIdLabel")

        # Labels must not intercept button clicks
        for label in (
            date_label,
            id_description_label,
            id_label,
        ):
            label.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents
            )

                # Layout
        self.main_layout.addWidget(date_label)
        self.main_layout.addStretch()
        self.main_layout.addWidget(id_description_label)
        self.main_layout.addWidget(id_label)
        # Style
        self.setStyleSheet("""
            SessionWidget {
                background-color: #f3f3f3;
                border: 1px solid #dddddd;
                border-radius: 8px;
                text-align: left;
            }

            SessionWidget:hover {
                background-color: #e5e5e5;
            }

            SessionWidget:pressed {
                background-color: #d8d8d8;
            }

            QLabel#sessionDateLabel {
                color: #111111;
                font-size: 17px;
                font-weight: 600;
                background-color: transparent;
            }

            QLabel#sessionIdDescriptionLabel {
                color: #aaaaaa;
                font-size: 12px;
                background-color: transparent;
            }

            QLabel#sessionIdLabel {
                color: #333333;
                font-size: 15px;
                font-weight: 600;
                background-color: transparent;
            }
        """)