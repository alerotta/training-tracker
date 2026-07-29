from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QLabel,
)

"""
Activity widget class, used to display activity main informations, name and
current nuber of sessions, when clicked the session page should be displayed.
"""

class ActivityWidget(QPushButton):

    # signal definition
    view_activity_request = Signal(int)

    def __init__(self, activiity: tuple[int,str] ,  session_number: int  = 0) -> None:

        super().__init__()

        # unpack argument
        self.activity_id, self.activity_name = activiity

        # create its own layout
        main_layout = QHBoxLayout(self)

        # create it internal component 
        activity_name_label = QLabel(self.activity_name)
        sessions_number_label = QLabel(str(self.activity_id))

        # add components to layout
        main_layout.addWidget(activity_name_label)
        main_layout.addWidget(sessions_number_label)

        # connect signal emit to click event
        self.clicked.connect(self._emit_signal)

    # function to emit the signal
    def _emit_signal(self):
        self.view_activity_request.emit(self.activity_id) 