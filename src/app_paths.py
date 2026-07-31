from pathlib import Path

from PySide6.QtCore import QStandardPaths


DATABASE_FILENAME = "training_tracker.db"


def get_app_data_directory() -> Path:
    """
    Return the operating-system-specific directory used for persistent
    application data.

    On macOS, this will normally be inside:
    ~/Library/Application Support/Training Tracker/
    """
    location = QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppDataLocation
    )

    if not location:
        raise RuntimeError(
            "Qt could not determine the application data directory."
        )

    directory = Path(location)
    directory.mkdir(parents=True, exist_ok=True)

    return directory


def get_database_path() -> Path:
    """Return the complete path of the SQLite database."""
    return get_app_data_directory() / DATABASE_FILENAME