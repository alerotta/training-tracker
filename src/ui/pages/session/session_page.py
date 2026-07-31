from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QStackedLayout,
)
from src.ui.pages.session.session_default_view import SessionDefaultView
from src.ui.pages.session.session_form_view import SessionFormView

class SessionPage (QWidget) :

    activity_page_request = Signal()
    add_new_session_request = Signal(str)

    def __init__(self, activity_name: str , sessions: list[tuple[int,str]] ) -> None:
        super().__init__()

        # create own layout
        self.stack_layout = QStackedLayout(self)

        #self.title_label = QLabel(activity_name)
        self.session_default_view = SessionDefaultView(activity_name,sessions)
        self.session_form_view = SessionFormView()

        # assign views to layout
        self.stack_layout.addWidget(self.session_default_view)
        self.stack_layout.addWidget(self.session_form_view)

        self._connect_signlas()

    def reload_sessions (self,sessions: list[tuple[int, str]]):
        self.session_default_view.session_container.reload_sessions(sessions)
        self.show_session_default_view()


    def _connect_signlas (self) -> None : 

        #signals from default view

        self.session_default_view.session_form_view_request.connect(
            self.show_session_form_view
        )

        # emit for get back to activities
        self.session_default_view.activity_page_request.connect(
            self.activity_page_request.emit
        )

        #signal from form view

        self.session_form_view.session_default_view_request.connect(
            self.show_session_default_view
        )

        self.session_form_view.add_new_session_request.connect(
            self.add_new_session_request.emit
        )

    def show_session_form_view (self) -> None:
        self.stack_layout.setCurrentWidget(self.session_form_view)

    def show_session_default_view (self) -> None:
        self.stack_layout.setCurrentWidget(self.session_default_view)