from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from src.ui.pages.activity.components.activity_widget import ActivityWidget

"""
Collects all activities elements and display them with a scrollbar, it mamanges all
activities common to all activity widgets, such as creation and init.
"""

class ActivityContainer (QWidget):

    def __init__(self, activities: list[tuple[int,str]]):
        super().__init__()

        self.main_layout = QVBoxLayout(self)

        # instance all activities
        for activity in activities:
            self.add_activity(activity)

    # function to create and add an actitivty to the container
    def add_activity(self,activiity: tuple[int,str] ,  session_number: int = 0) -> None:

        activity_widget = ActivityWidget(activiity,session_number)
        self.main_layout.addWidget(activity_widget)

    def reload_activities (self, activities: list[tuple[int,str]]) -> None :

        #clear all widgets
        while self.main_layout.count() > 0:
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        #re instance
        for activity in activities:
            self.add_activity(activity)