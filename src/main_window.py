from src.db.database import get_all_activities, create_activity
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QLabel
)
from src.ui.pages.activity.activity_page import ActivityPage

"""
main controll class, it cordinates the ui and the database values, it is responsible to control
which ui page is shown and interact with the database
"""

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Training Tracker")
        self.resize(1000,700)

        #debug = QLabel("debug")
        #self.page_stack.addWidget(debug)

        # fetch activities from db and create activity page
        activities = get_all_activities()
        self.activity_page = ActivityPage(activities)

        # create stack layout and add the actitivty page
        self.page_stack = QStackedWidget()
        
        self.page_stack.addWidget(self.activity_page)
      
        # set the contral widget and show the window
        self.setCentralWidget(self.page_stack)

        self._connect_signals()

    #connect received signals to class methods
    def _connect_signals (self) -> None:
        self.activity_page.activity_add_request.connect(
            self.add_activity_to_database
        )

    def add_activity_to_database(self,txt: str):
        create_activity(txt)

        #refetch and reload activities
        activities = get_all_activities()
        self.activity_page.reload_activities(activities)
        


    




