from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
from .data_ingestion import DataIngestion
from .data_transformation import DataTransformation

class ModelTrainer:
    def __init__(self, db_path="db.sqlite3", model_path="models/spam_model.pkl"):
        self.db_path = db_path
        self.model_path = model_path

    def train_model(self):
        # Load data
        ingestor = DataIngestion(self.db_path)
        df = ingestor.load_data()

        # Transform data
        transformer = DataTransformation()
        X, y = transformer.transform(df)

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train classifier
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        # Save model and transformer
        import os
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, self.model_path)
        joblib.dump(transformer, "models/tfidf_transformer.pkl")
        print(f"Model saved at {self.model_path}")
