
from PySide6.QtWidgets import (
    QWidget,
    QStackedLayout
)
from src.ui.pages.activity.activity_default_view import ActivityDefaultView
from src.ui.pages.activity.activity_form_view import ActivityFormView


""" 
Activity Page contains all possible views related to the activities, for example the default
and the form view, this class in responsible to define how to switch between views related to the page
"""

class ActivityPage (QWidget) :


    def __init__(self, activities: list[tuple[int,str]]) -> None:
        super().__init__()

        # create own layout
        self.stack_layout = QStackedLayout(self)

        # create managed views
        self.activity_default_view = ActivityDefaultView(activities)
        self.activity_form_view = ActivityFormView()

        # assign views to layout
        self.stack_layout.addWidget(self.activity_default_view)
        self.stack_layout.addWidget(self.activity_form_view)

        # connect signals
        self._connect_signlas()

    def _connect_signlas (self) -> None : 

        self.activity_default_view.activity_form_request.connect(
            self.show_activity_form_view
        )

        self.activity_form_view.activity_default_request.connect(
            self.show_activity_default_view
        )

    def show_activity_default_view(self):
        self.stack_layout.setCurrentWidget(self.activity_default_view)

    def show_activity_form_view(self):
        self.stack_layout.setCurrentWidget(self.activity_form_view)