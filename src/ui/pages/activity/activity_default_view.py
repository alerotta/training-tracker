from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
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

        # create components
        add_button = QPushButton("New Actitivty")
        add_button.clicked.connect(
            self.activity_form_request.emit
        )
        self.activity_container = ActivityContainer(activities)

        # add components to layout
        self.main_layout.addWidget(add_button)
        self.main_layout.addWidget(self.activity_container)

        self.activity_container.view_activity_sessions_request.connect(
            self.view_activity_sessions_request.emit
        )