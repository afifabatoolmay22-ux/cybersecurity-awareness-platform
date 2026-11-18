import sqlite3
from config import Config


def get_db_connection():
    """Open a connection to the SQLite database and return it."""
    conn = sqlite3.connect(Config.DATABASE)
    # This lets us read columns by name, e.g. row["email"]
    conn.row_factory = sqlite3.Row
    # Turn on foreign key checking (SQLite has it off by default)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn