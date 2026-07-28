from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)

class ActivityWidget(QWidget):
    def __init__(self, activiity_name: str ,  session_number: int  = 0) -> None:
        super().__init__()
        main_layout = QHBoxLayout(self)

        activity_name = QLabel(activiity_name)
        sessions_number = QLabel(str(session_number))

        main_layout.addWidget(activity_name)
        main_layout.addWidget(sessions_number)
