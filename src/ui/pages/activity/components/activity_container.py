from PySide6.QtCore import Signal , Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
)
from src.ui.pages.activity.components.activity_widget import ActivityWidget

"""
Collects all activities elements and display them with a scrollbar, it mamanges all
activities common to all activity widgets, such as creation and init.
"""

class ActivityContainer (QWidget):

    view_activity_sessions_request = Signal(int)
    
    def __init__(self, activities: list[tuple[int,str]]):
        super().__init__()

        #main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Scrollable area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Widget placed inside the scroll area
        self.scroll_content = QWidget()

        # Layout that contains the activity buttons
        self.activities_layout = QVBoxLayout(self.scroll_content)
        self.activities_layout.setContentsMargins(10, 10, 10, 10)
        self.activities_layout.setSpacing(8)
        self.activities_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        self.scroll_area.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll_area)

        # instance all activities
        for activity in activities:
            self.add_activity(activity)

    # function to create and add an actitivty to the container
    def add_activity(self,activiity: tuple[int,str] ,  session_number: int = 0) -> None:

        activity_widget = ActivityWidget(activiity,session_number)
        activity_widget.view_activity_sessions_request.connect(
            self.view_activity_sessions_request.emit
        )
        self.activities_layout.addWidget(activity_widget)

    def reload_activities (self, activities: list[tuple[int,str]]) -> None :

        self.clear_activities()
        #re instance
        for activity in activities:
            self.add_activity(activity)

    def clear_activities (self) -> None :

        #clear all widgets
        while self.activities_layout.count() > 0:
            item = self.activities_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
