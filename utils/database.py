import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load environment variables from .env file located in the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(os.getenv('DATABASE_URL'))
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def query(self, sql, params=None):
        try:
            if not self.conn or self.conn.closed != 0:
                self.connect()
            self.cur.execute(sql, params or ())
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e

    def fetch(self):
        return self.cur.fetchall()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
