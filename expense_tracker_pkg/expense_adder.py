import logging
from .db_manager import get_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_expense(db_path, description, amount, date, category=None):
    """Add a new expense to the database."""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to the database.")
            return False

        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO expenses (description, amount, date, category)
            VALUES (?, ?, ?, ?);
        ''', (description, amount, date, category))
        connection.commit()
        connection.close()
        logging.info(f"Expense added successfully: {description}, {amount}, {date}, {category}")
        return True
    except Exception as e:
        logging.error(f"Error adding expense: {e}")
        return False
    
    cursor = connection.commit
    
