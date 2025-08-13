# utils/test_db_connection.py

from database import Database

def test_database_connection():
    try:
        with Database() as db:
            print("Connected to PostgreSQL database successfully!")
            # Perform a test query
            db.query("SELECT version();")
            result = db.fetch()
            print("PostgreSQL database version:", result[0])
    except Exception as e:
        print("Error connecting to PostgreSQL database:", e)

if __name__ == "__main__":
    test_database_connection()
