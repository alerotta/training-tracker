from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QDateEdit,
    QSizePolicy,
)

class SessionFormView (QWidget):

    session_default_view_request = Signal()
    add_new_session_request = Signal(str)

    def __init__(self):
        super().__init__()

        # Main vertical layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)


        # First row: label and date input
        date_layout = QHBoxLayout()
        date_layout.setSpacing(12)

        self.date_label = QLabel("Select Date:")
        self.date_label.setObjectName("sessionDateLabel")

        self.date_input = QDateEdit()
        self.date_input.setObjectName("sessionDateInput")
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setDisplayFormat("dd/MM/yyyy")
        self.date_input.setMinimumHeight(45)

        date_layout.addWidget(self.date_label)
        date_layout.addWidget(self.date_input, stretch=1)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)

        self.add_button = QPushButton("Add Session")
        self.add_button.setObjectName("addSessionButton")

        self.cancel_button = QPushButton("Back")
        self.cancel_button.setObjectName("cancelSessionButton")

        for button in (
            self.add_button,
            self.cancel_button,
        ):
            button.setMinimumHeight(70)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed,
            )

        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.cancel_button)

        # Add rows to main layout
        self.main_layout.addLayout(date_layout)
        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addStretch()

        # Signals
        self.add_button.clicked.connect(
            self.new_session_request
        )

        self.cancel_button.clicked.connect(
            self.session_default_view_request.emit
        )

        self.setStyleSheet("""
            QLabel#sessionDateLabel {
                color: #111111;
                font-size: 15px;
                font-weight: 600;
                background-color: transparent;
            }

            QDateEdit#sessionDateInput {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 8px;
                padding: 0 12px;

                color: #111111;
                font-size: 15px;
            }

            QDateEdit#sessionDateInput:hover {
                border: 1px solid #aaaaaa;
            }

            QDateEdit#sessionDateInput:focus {
                border: 1px solid #777777;
            }

            QDateEdit#sessionDateInput::drop-down {
                width: 32px;
                border: none;
                border-left: 1px solid #dddddd;
            }

            QPushButton#addSessionButton,
            QPushButton#cancelSessionButton {
                background-color: #f3f3f3;
                border: 1px solid #dddddd;
                border-radius: 8px;

                color: #111111;
                font-size: 17px;
                font-weight: 600;
            }

            QPushButton#addSessionButton:hover{
                background-color: #E8F2E6;
            }

            QPushButton#cancelSessionButton:hover{
                background-color: #F2E1E1;
            }

            QPushButton#addSessionButton:pressed{
                background-color: #D1DECE;
            }

            QPushButton#cancelSessionButton:pressed{
                background-color: #E3D5D5;
            }
        """)


    def new_session_request(self):
        date = self.date_input.text()
        self.add_new_session_request.emit(date)

        

