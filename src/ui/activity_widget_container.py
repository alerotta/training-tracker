from src.ui.activity_widget import ActivityWidget
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)

class ActivityWidgetContainer(QWidget):

    add_new_activity_request = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.main_layout = QVBoxLayout(self)

        add_activity_button = QPushButton(" New Activity")
        add_activity_button.clicked.connect(
            self.add_new_activity_request.emit
        )

        self.activities_layout = QVBoxLayout()

        self.main_layout.addWidget(add_activity_button)
        self.main_layout.addLayout(self.activities_layout)

    def set_activities_widgets (self, activity_names: list[str]) -> None:
        self.clear_activity_widgets()
        for name in activity_names:
            self.activities_layout.addWidget(ActivityWidget(name))
        return

    def crearte_new_activity (self, name:str) -> None:
        self.activities_layout.addWidget(ActivityWidget(name))
        return

    def clear_activity_widgets(self) -> None:
        while self.activities_layout.count() > 0:
            item = self.activities_layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()