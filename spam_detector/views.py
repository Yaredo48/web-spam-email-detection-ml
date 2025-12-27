from django.shortcuts import render
from src.pipeline.predict_pipeline import PredictPipeline

pipeline = PredictPipeline()

def predict_email(request):
    prediction = None
    if request.method == "POST":
        subject = request.POST.get("subject", "")
        body = request.POST.get("body", "")
        prediction = pipeline.predict(subject, body)

    return render(request, "predict.html", {"prediction": prediction})
