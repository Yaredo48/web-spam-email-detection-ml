from src.pipeline.predict_pipeline import PredictPipeline

pipeline = PredictPipeline()

subject = "Congratulations! You won a free iPhone"
body = "Click the link below to claim your prize now!"

print("Prediction:", pipeline.predict(subject, body))
