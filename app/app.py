from flask import Flask, render_template, request
import joblib
from pathlib import Path
import os  

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer safely
models_dir = Path(__file__).resolve().parent.parent / "models"
model_path = models_dir / "classifier_model.pkl"
vectorizer_path = models_dir / "text_vectorizer.pkl"

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["user_text"]

    # Transform text and predict
    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)[0]
    probs = model.predict_proba(text_tfidf)[0]
    confidence = max(probs) * 100

    return render_template(
        "result.html",
        text=text,
        prediction=prediction,
        confidence=f"{confidence:.2f}%"
    )

@app.route("/topics")
def topics():
    return render_template("topics.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)


