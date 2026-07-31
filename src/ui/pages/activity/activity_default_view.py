from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QSizePolicy
)
from src.ui.pages.activity.components.activity_container import ActivityContainer

class ActivityDefaultView (QWidget):

    activity_form_request = Signal()
    view_activity_sessions_request = Signal(int)
    activity_container : ActivityContainer

    def __init__(self, activities: list[tuple[int,str]]):
        super().__init__()

        # create own layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        # create components
        add_button = QPushButton("New Activity")
        add_button.setObjectName("newActivityButton")
        add_button.setMinimumHeight(70)
        add_button.setCursor(Qt.CursorShape.PointingHandCursor)

        add_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        add_button.setStyleSheet("""
            QPushButton#newActivityButton {
                background-color: #f3f3f3;
                border: 1px solid #dddddd;
                border-radius: 8px;

                color: #111111;
                font-size: 17px;
                font-weight: 600;

                text-align: left;
                padding-left: 20px;
            }

            QPushButton#newActivityButton:hover {
                background-color: #E8F2E6;
            }

            QPushButton#newActivityButton:pressed {
                background-color: #D1DECE;
            }
        """)

        add_button.clicked.connect(
            self.activity_form_request.emit
        )
        self.activity_container = ActivityContainer(activities)

        # add components to layout
        self.main_layout.addWidget(add_button)
        self.main_layout.addWidget(self.activity_container,stretch=1,)

        self.activity_container.view_activity_sessions_request.connect(
            self.view_activity_sessions_request.emit
        )

