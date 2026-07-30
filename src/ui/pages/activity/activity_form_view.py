from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QLabel
)

class ActivityFormView (QWidget):

    activity_default_view_request = Signal()
    activity_add_request = Signal(str)

    def __init__(self):
        super().__init__()

        #create own layout
        self.main_layout = QHBoxLayout(self)

        # create components
        self.cancel = QPushButton("Cancel")
        self.add = QPushButton("ADD")
        self.text_line = QLineEdit()
        self.text_label = QLabel("Activity Name:")


        self.cancel.clicked.connect(
            self.cancel_activity_request
        )

        self.add.clicked.connect(
            self.new_activity_request
        )

        self.main_layout.addWidget(self.text_label)
        self.main_layout.addWidget(self.text_line)
        self.main_layout.addWidget(self.add)
        self.main_layout.addWidget(self.cancel)


    def new_activity_request (self) -> None:
        txt = self.text_line.text()
        self.text_line.clear()
        self.activity_add_request.emit(txt)
        return

    def cancel_activity_request (self) -> None:
        self.text_line.clear()
        self.activity_default_view_request.emit()
        return
