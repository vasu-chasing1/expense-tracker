import logging 
from .db_manager import get_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def view_all_expenses(db_path):
    """View all expenses from the database"""

    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database.")
            return []
        cursor = connection.cursor()

        cursor.execute("""
                       SELECT * FROM expenses ORDER BY date DESC;
                       """)
        
        results = cursor.fetchall()
        connection.close()
        return results
    
    except Exception as e:
        logging.error(f"Error viewing expenses: {e}")
        return []
    
def view_expenses_by_category(db_path, category):
    """View expenses filtered by category"""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database.")
            return []
        cursor = connection.cursor()

        cursor.execute("""
    SELECT * FROM expenses WHERE category = ? ORDER BY date DESC;
""", (category,))
        
        results = cursor.fetchall()
        connection.close()
        return results
        
    except Exception as e:
        logging.error(f"Error viewing expenses: {e}")
        return []



