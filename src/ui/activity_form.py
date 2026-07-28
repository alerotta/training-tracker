from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)

class ActivityForm(QWidget):

    create_new_activity_request = Signal(str)
    cancel_activity_creation_request = Signal()
    
       
    def __init__ (self) -> None:
        
        super().__init__()

        self.label = QLabel("Activity Name:")
        self.line_edit = QLineEdit()

        add_button = QPushButton("ADD")
        add_button.clicked.connect(
            self.request_new_activity_creation
        )

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(
            self.cancel_activity_creation_request.emit
        )

        main_layout = QHBoxLayout(self)
        #add components
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(add_button)
        main_layout.addWidget(cancel_button)

    def request_new_activity_creation (self) -> None:
        activity_name = self.line_edit.text().strip()
        if not activity_name :
            return
        self.line_edit.clear()
        self.create_new_activity_request.emit(activity_name)

