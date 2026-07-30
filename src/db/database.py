import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIRECTORY = PROJECT_ROOT / "data"
DATABASE_PATH = DATA_DIRECTORY / "training_tracker.db"

def get_connection() -> sqlite3.Connection:
    DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def initialize_database() -> None:
    connection = get_connection()
    try: 
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,

                UNIQUE (name)
            );

            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity_id INTEGER NOT NULL,
                session_date TEXT NOT NULL,

                FOREIGN KEY (activity_id)
                    REFERENCES activities(id)
                    ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS activity_fields (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                data_type TEXT NOT NULL,
                unit TEXT,
                is_required INTEGER NOT NULL DEFAULT 0,

                FOREIGN KEY (activity_id)
                    REFERENCES activities(id)
                    ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS session_field_values (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                activity_field_id INTEGER NOT NULL,
                value_text TEXT,

                FOREIGN KEY (session_id)
                    REFERENCES sessions(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (activity_field_id)
                    REFERENCES activity_fields(id)
                    ON DELETE CASCADE,

                UNIQUE (session_id, activity_field_id)
            );
            """
        )
    finally:
        connection.close

def create_activity(name: str) -> int:
    
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO activities (name)
            VALUES (?)
            """,
            (name,),
        )

        activity_id = cursor.lastrowid

        if activity_id is None:
            raise RuntimeError(
                "The activity was not created correctly."
            )

        return activity_id

def create_session(activity_id: int, session_date: str) -> int:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO sessions (activity_id, session_date)
            VALUES (?, ?)
            """,
            (
                activity_id,
                session_date,
            ),
        )

        session_id = cursor.lastrowid

        if session_id is None:
            raise RuntimeError(
                "The session was not created correctly."
            )

        return session_id

def get_all_activities() -> list[sqlite3.Row]:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id, name
            FROM activities
            ORDER BY name
            """
        )

        rows = cursor.fetchall()

    return [
        (row["id"], row["name"])
        for row in rows
    ]

def get_activity_name(activity_id: int) -> str:
    with get_connection() as connection:
        cursor = connection.execute(
            "SELECT name FROM activities WHERE id = ?",
            (activity_id,),
        )
        row = cursor.fetchone()

        if row is None:
            raise ValueError(f"Activity with ID {activity_id} not found")

        return row[0]

def get_all_sessions(activity_id: int) -> list[tuple[int, str]]:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            SELECT id, session_date
            FROM sessions
            WHERE activity_id = ?
            ORDER BY session_date
            """,
            (activity_id,),
        )

        rows = cursor.fetchall()

    return [
        (row["id"], row["session_date"])
        for row in rows
    ]
