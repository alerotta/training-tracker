from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget
)
from src.ui.activity_widget_container import ActivityWidgetContainer
from src.ui.activity_form import ActivityForm

class MainWindow(QMainWindow):

    create_new_activity_request = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Training Tracker")
        self.resize(1000,700)

        self.activity_widget_container = ActivityWidgetContainer()
        self.activity_form = ActivityForm()

        self.page_stack = QStackedWidget()
        self.page_stack.addWidget(self.activity_widget_container)
        self.page_stack.addWidget(self.activity_form)

        self.setCentralWidget(self.page_stack)
        self._connect_signals()
        self.show()

    def init_activity_widget_container(self, activity_names: list[str]) -> None:
        self.activity_widget_container.set_activities_widgets(activity_names)
        return

    def _connect_signals(self) -> None:

        ## activity container signals 

        self.activity_widget_container.add_new_activity_request.connect(
            self.show_activity_form
        )

        ## activity from signals

        self.activity_form.create_new_activity_request.connect(
            ## re-emit signal to the controller
            self.create_new_activity_request.emit
        )

        self.activity_form.cancel_activity_creation_request.connect(
            self.show_activity_container
        )

    def show_activity_container (self) -> None:
        self.page_stack.setCurrentWidget(self.activity_widget_container)

    def show_activity_form (self) -> None:
        self.page_stack.setCurrentWidget(self.activity_form)

