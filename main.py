import sys
from src.db.database import initialize_database
from src.controllers.controller import Controller
from PySide6.QtWidgets import QApplication

def main() -> int:
    initialize_database()
    application = QApplication(sys.argv)
    controller = Controller()
    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())
