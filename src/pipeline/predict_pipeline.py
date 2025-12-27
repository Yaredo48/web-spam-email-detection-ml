import joblib
import pandas as pd
from src.components.data_transformation import DataTransformation

class PredictPipeline:
    def __init__(self, model_path="models/spam_model.pkl", transformer_path="models/tfidf_transformer.pkl"):
        self.model = joblib.load(model_path)
        self.transformer = joblib.load(transformer_path)
        self.transformer_class = DataTransformation()  # For text cleaning

    def predict(self, email_subject, email_body):
        # Combine and clean text
        content = f"{email_subject} {email_body}"
        content_clean = self.transformer_class.clean_text(content)

        # Transform using saved TF-IDF
        X = self.transformer.transformer.transform([content_clean])

        # Predict
        prediction = self.model.predict(X)[0]
        return "Spam" if prediction == 1 else "Ham"
