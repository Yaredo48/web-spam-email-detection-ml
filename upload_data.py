import sqlite3
import pandas as pd

#conect to sqlite DB

conn=sqlite3.connect("db.sqlite3")
cursor=conn.cursor()


# Load CSV dataset
data = pd.read_csv("dataset/spam_emails.csv")  # CSV must have: sender, subject, body, is_spam


# Insert into DB
for _, row in data.iterrows():
    cursor.execute("""
        INSERT INTO spam_detector_email (sender, subject, body, is_spam)
        VALUES (?, ?, ?, ?)
    """, (row['sender'], row['subject'], row['body'], row['is_spam']))

conn.commit()
conn.close()

print("data uploaded successfuly")