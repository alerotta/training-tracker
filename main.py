import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Training Tracker")
        self.resize(900,600)
        label = QLabel("Training Tracker Test!")
        self.setCentralWidget(label)


def main() -> int:
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())
