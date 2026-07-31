from PySide6.QtCore import Signal , Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QSizePolicy,
)

class ActivityFormView (QWidget):

    activity_default_view_request = Signal()
    activity_add_request = Signal(str)

    def __init__(self):
        super().__init__()

        #create own layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # First row: label and line edit
        input_layout = QHBoxLayout()
        input_layout.setSpacing(12)


        self.text_label = QLabel("Activity Name:")
        self.text_label.setObjectName("activityNameLabel")

        self.text_line = QLineEdit()
        self.text_line.setObjectName("activityNameInput")
        self.text_line.setPlaceholderText("Enter activity name")
        self.text_line.setMinimumHeight(45)

        input_layout.addWidget(self.text_label)
        input_layout.addWidget(self.text_line, stretch=1)

        # Second row: action buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)

        self.add = QPushButton("Add Activity")
        self.add.setObjectName("addActivityButton")

        self.cancel = QPushButton("Cancel")
        self.cancel.setObjectName("cancelActivityButton")

        for button in (self.add, self.cancel):
            button.setMinimumHeight(70)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed,
            )

        buttons_layout.addWidget(self.add)
        buttons_layout.addWidget(self.cancel)

        # Add both rows to the main layout
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addStretch()


        self.cancel.clicked.connect(
            self.cancel_activity_request
        )

        self.add.clicked.connect(
            self.new_activity_request
        )

        # Styling
        self.setStyleSheet("""
            QLabel#activityNameLabel {
                color: #111111;
                font-size: 15px;
                font-weight: 600;
                background-color: transparent;
            }

            QLineEdit#activityNameInput {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 8px;
                padding: 0 12px;

                color: #111111;
                font-size: 15px;
            }

            QLineEdit#activityNameInput:hover {
                border: 1px solid #aaaaaa;
            }

            QLineEdit#activityNameInput:focus {
                border: 1px solid #777777;
            }

            QPushButton#addActivityButton,
            QPushButton#cancelActivityButton {
                background-color: #f3f3f3;
                border: 1px solid #dddddd;
                border-radius: 8px;

                color: #111111;
                font-size: 17px;
                font-weight: 600;
            }

            QPushButton#addActivityButton:hover{
                background-color: #E8F2E6;
            }

            QPushButton#cancelActivityButton:hover{
                background-color: #F2E1E1;
            }

            QPushButton#addActivityButton:pressed{
                background-color: #D1DECE;
            }

            QPushButton#cancelActivityButton:pressed{
                background-color: #E3D5D5;
            }

        """)




    def new_activity_request (self) -> None:
        txt = self.text_line.text()
        self.text_line.clear()
        self.activity_add_request.emit(txt)
        return

    def cancel_activity_request (self) -> None:
        self.text_line.clear()
        self.activity_default_view_request.emit()
        return
