import sqlite3
import logging
from .db_manager import get_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def delete_expense(db_path, expense_id):
    """Delete an expense by id"""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database")
            return False
        
        cursor = connection.cursor()
        cursor.execute('''
                       DELETE FROM expenses WHERE id = ?
                       ''', (int(expense_id),))
        connection.commit()
        connection.close()
        logging.info(f"Expense with ID {expense_id} deleted successfully.")
        return True
        
    except Exception as e:
        logging.error(f"Error deleting expense: {e}")
        return False
