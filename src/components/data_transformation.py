from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re

class DataTransformation:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

        def clean_text(self,text):
            text=str(text).lower()
            text = re.sub(r'\W', ' ', text)  # Remove special characters
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        

        def transform(self, df: pd.DataFrame):
            # Combine subject + body
            df['content'] = df['subject'].fillna('') + ' ' + df['body'].fillna('')
            df['content'] = df['content'].apply(self.clean_text)

            X = self.vectorizer.fit_transform(df['content'])
            y = df['is_spam'].astype(int)
            return X, y