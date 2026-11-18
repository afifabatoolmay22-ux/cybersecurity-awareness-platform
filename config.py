import os
from dotenv import load_dotenv

# Folder where this file lives
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Read the values from the .env file
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    # Secret key used to protect sessions (login cookies)
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Location of the SQLite database file
    DATABASE = os.path.join(BASE_DIR, "instance", "database.db")

    # Safer cookie settings
    SESSION_COOKIE_HTTPONLY = True      # JavaScript cannot read the session cookie
    SESSION_COOKIE_SAMESITE = "Lax"     # Helps protect against CSRF attacks