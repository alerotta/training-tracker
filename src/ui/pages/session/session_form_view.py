from PySide6.QtCore import Signal
from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QDateEdit,
)

class SessionFormView (QWidget):

    session_default_view_request = Signal()
    add_new_session_request = Signal(str)

    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout(self)

        self.date_label = QLabel("Select Date")

        self.date_input = QDateEdit()        
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setDisplayFormat("dd/MM/yyyy")

        self.add_button = QPushButton("Add session")
        self.add_button.clicked.connect(
            self.new_session_request
        )

        self.cancel_button = QPushButton("back")
        self.cancel_button.clicked.connect(
            self.session_default_view_request.emit
        )

        self.main_layout.addWidget(self.date_label)
        self.main_layout.addWidget(self.date_input)
        self.main_layout.addWidget(self.add_button)
        self.main_layout.addWidget(self.cancel_button)

    def new_session_request(self):
        date = self.date_input.text()
        self.add_new_session_request.emit(date)

        

