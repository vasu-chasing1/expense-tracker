import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_db(db_path):
    """Create the database and expense table if they don't exist."""
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       description TEXT NOT NULL,
                          amount REAL NOT NULL,
                            date TEXT NOT NULL,
                       category TEXT 
            );
        ''')
        connection.commit()
        connection.close()
        logging.info(f"Database initialized successfully. at: {db_path}")
    except Exception as e:
        logging.error(f"Error initializing database: {e}")

def get_connection(db_path):
    """Get a connection to the database."""
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except Exception as e:
        logging.error(f"Error connecting to database: {e}")
        return None