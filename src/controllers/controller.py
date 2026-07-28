# src/activity_controller.py

from PySide6.QtCore import QObject
from src.ui.main_window import MainWindow
from src.db.database import *


class Controller(QObject):

    def __init__(self,) -> None:
        super().__init__()

        self.main_window = MainWindow()
        self.load_all_activities()
        self._connect_signals()


    def load_all_activities(self) -> None:
        try:
            activities = get_all_activities()
        except Exception as error:
            print(f"Could not load activities: {error}")
            return

        activity_names = [
            activity["name"]
            for activity in activities
        ]

        self.main_window.init_activity_widget_container(activity_names)

    def _connect_signals(self) -> None:
        self.main_window.create_new_activity_request.connect(
            self.create_activity
        )

    def create_activity (self, activity_name : str) -> None:
        create_activity(activity_name)
        self.load_all_activities()

        


