from PySide6.QtCore import Signal , Qt
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
    view_activity_sessions_request = Signal(int)

    def __init__(self, activiity: tuple[int,str] ,  session_number: int  = 0) -> None:

        super().__init__()

        # unpack argument
        self.activity_id, self.activity_name = activiity

        # Button configuration
        self.setMinimumHeight(70)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # create its own layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 10, 20, 10)
        main_layout.setSpacing(8)

        # create it internal component 
        activity_name_label = QLabel(self.activity_name)
        activity_name_label.setObjectName("activityNameLabel")

        session_counter_label = QLabel("Session counter:")
        session_counter_label.setObjectName("sessionCounterLabel")

        sessions_number_label = QLabel(str(self.activity_id))
        sessions_number_label.setObjectName("sessionsNumberLabel")

        # Ensure the QPushButton receives clicks made over the labels
        for label in (
            activity_name_label,
            session_counter_label,
            sessions_number_label,
        ):
            label.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents
            )

        # Layout arrangement
        main_layout.addWidget(activity_name_label)
        main_layout.addStretch()
        main_layout.addWidget(session_counter_label)
        main_layout.addWidget(sessions_number_label)

        # Styling
        self.setStyleSheet("""
            ActivityWidget {
                background-color: #f3f3f3;
                border: 1px solid #dddddd;
                border-radius: 20px;
                text-align: left;
            }

            ActivityWidget:hover {
                background-color: #e5e5e5;
            }

            ActivityWidget:pressed {
                background-color: #d8d8d8;
            }

            QLabel#activityNameLabel {
                color: #111111;
                font-size: 17px;
                font-weight: 600;
                background-color: transparent;
            }

            QLabel#sessionCounterLabel {
                color: #aaaaaa;
                font-size: 12px;
                background-color: transparent;
            }

            QLabel#sessionsNumberLabel {
                color: #333333;
                font-size: 15px;
                font-weight: 600;
                background-color: transparent;
            }
        """)


        # connect signal emit to click event
        self.clicked.connect(self._emit_signal)

    # function to emit the signal
    def _emit_signal(self):
        self.view_activity_sessions_request.emit(self.activity_id) 