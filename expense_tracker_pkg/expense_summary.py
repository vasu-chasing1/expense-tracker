import logging
from .db_manager import get_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_total_spent(db_path):
    """Get total amount spent on all expenses"""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database")
            return 0
        
        cursor = connection.cursor()
        cursor.execute('''
                       SELECT SUM(amount) FROM expenses;
                       ''')
        result = cursor.fetchone()
        connection.close()
        return result[0] if result[0] else 0
    
    except Exception as e:
        logging.error(f"Error getting total spend: {e}")
        return 0
    
def get_average_expense(db_path):
    """Get average expense amount"""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database")
            return 0
        
        cursor = connection.cursor()
        cursor.execute('''
                       SELECT AVG(amount) FROM expenses;
                       ''')
        
        result = cursor.fetchone()
        connection.close()
        return result[0] if result[0] else 0
    
    except Exception as e:
        logging.error(f"Error getting average expense: {e}")
        return 0
    
def get_expense_count(db_path):
    """Get total number of expense"""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database")
            return 0
        cursor = connection.cursor()

        cursor.execute('''
                       SELECT COUNT(*) FROM expenses;
                       ''')
        result = cursor.fetchone()
        connection.close()
        return result[0] if result[0] else 0
        
    except Exception as e:
        logging.error(f"Error getting expense count: {e}")
        return 0
    

def get_summary_by_category(db_path):
    """Get total spent grouped by category"""
    try:
        connection = get_connection(db_path)
        if connection is None:
            logging.error("Failed to connect to database.")
            return []
        
        cursor = connection.cursor() 
        cursor.execute('''SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC;
                       '''
                       )
        results = cursor.fetchall()
        connection.close()
        return results
        
    except Exception as e:
        logging.error(f"Error getting summary by category: {e}")
        return []