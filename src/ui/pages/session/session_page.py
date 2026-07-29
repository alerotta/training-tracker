from PySide6.QtWidgets import (
    QWidget,
    QStackedLayout,
)

class SessionPage (QWidget) :

    def __init__(self) -> None:
        super().__init__()

        self.stack_layout = QStackedLayout()