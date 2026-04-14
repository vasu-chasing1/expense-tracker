from expense_tracker_pkg.db_manager import init_db
from expense_tracker_pkg.main import run

if __name__ == "__main__":
    db_path = "expenses.db"
    
    # Initialize database
    init_db(db_path)
    
    # Start the application
    run(db_path)