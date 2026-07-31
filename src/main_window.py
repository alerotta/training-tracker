from src.db.database import (
    get_all_activities, 
    create_activity,
    get_all_sessions,
    get_activity_name,
    create_session)
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QLabel
)
from src.ui.pages.activity.activity_page import ActivityPage
from src.ui.pages.session.session_page import SessionPage

"""
main controll class, it cordinates the ui and the database values, it is responsible to control
which ui page is shown and interact with the database
"""

class MainWindow(QMainWindow):

    sessions_page : SessionPage
    current_activity_id : int

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Training Tracker")
        self.resize(1000,700)


        # fetch activities from db and create activity page
        activities = get_all_activities()
        self.activity_page = ActivityPage(activities)

        # create stack layout and add the actitivty page
        self.page_stack = QStackedWidget()
        
        self.page_stack.addWidget(self.activity_page)
      
        # set the contral widget and show the window
        self.setCentralWidget(self.page_stack)

        self._connect_signals_activity_page()
        

    def add_activity_to_database(self,txt: str):
        # create in database new row
        create_activity(txt)

        #refetch and reload activities
        activities = get_all_activities()
        self.activity_page.reload_activities(activities)
        return

    def add_session_to_database(self, date: str) -> None:
        # create in database new row
        create_session(self.current_activity_id,date)

        #refetch and reload activities
        sessions = get_all_sessions(self.current_activity_id)
        self.sessions_page.reload_sessions(sessions)
        return
        

    def show_activity_page(self):
        self.page_stack.setCurrentWidget(self.activity_page)

    def show_session_page(self,activity_id:int):

        self.current_activity_id = activity_id
        self.current_activity_name = get_activity_name(activity_id)

        sessions = get_all_sessions(activity_id)
        self.sessions_page = SessionPage(self.current_activity_name,sessions )
        self._connect_signals_session_page ()
        self.page_stack.addWidget(self.sessions_page)
        self.page_stack.setCurrentWidget(self.sessions_page)
        return

    #connect received signals to class methods
    def _connect_signals_activity_page (self) -> None:

        self.activity_page.activity_add_request.connect(
            self.add_activity_to_database
        )

        self.activity_page.view_activity_sessions_request.connect(
            self.show_session_page
        )

    def _connect_signals_session_page (self) -> None:

        self.sessions_page.activity_page_request.connect(
            self.show_activity_page
        )

        self.sessions_page.add_new_session_request.connect(
            self.add_session_to_database
        )
    