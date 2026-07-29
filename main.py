import sys
from src.db.database import initialize_database
from src.main_window import MainWindow
from PySide6.QtWidgets import QApplication

def main() -> int:
    initialize_database()
    application = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())
