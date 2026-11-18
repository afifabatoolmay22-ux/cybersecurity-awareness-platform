from flask import Flask, render_template
from config import Config
from database import get_db_connection

# Create the Flask application and load the settings
app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    """Home page."""
    return render_template("index.html")


@app.route("/health")
def health():
    """A test page that checks Flask and the database connection."""
    conn = get_db_connection()
    conn.execute("SELECT 1")
    conn.close()
    return "Flask is running and the SQLite connection works."


if __name__ == "__main__":
    # debug=True auto-reloads the server when you edit code.
    # It is for development only and is switched off at deployment (Stage 10).
    app.run(debug=True)