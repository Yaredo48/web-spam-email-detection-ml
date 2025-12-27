import sqlite3
import pandas as pd

class DataIngestion:
    def __init__(self,db_path="db.sqlite3"):
        self.db_path=db_path

    def load_data(self):
        """Load emails from SQLite database"""
        conn=sqlite3.connect(self.db_path)
        query="SELECT sender, subject, body, is_spam FROM spam_detector_email"
        df = pd.read_sql(query, conn)
        conn.close()
        return df