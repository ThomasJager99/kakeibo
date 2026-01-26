import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv

#loading path to lib
env_path=Path(__file__).resolve().parent.parent / 'shadow_kakeibo' / '.env'
load_dotenv(env_path)

#Taking environment values out of there
db_path=os.getenv("KAKEIBO_DB_PATH")

#this one for errors
if not db_path:
    raise RuntimeError("KAKEIBO_DB_PATH is not set")

#this one for connection
def get_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

#this one for creating a table
def init_bd():
    with get_connection() as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS expenses(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    currency TEXT NOT NULL,
                    note TEXT,
                    category TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """
        )
        conn.commit()

