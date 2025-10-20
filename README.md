News Bias Classifier
Overview

This project is a Flask web application that predicts whether a short piece of news text is more likely to come from CNN or Fox News.
It was developed as part of the ADS509 final project to demonstrate an end-to-end machine learning workflow that includes data preparation, model training, evaluation, and deployment.

What It Does:

Cleans and vectorizes text using TF-IDF.

Trains a logistic regression classifier to distinguish between CNN and Fox News content.

Provides a simple web interface for entering text and viewing predictions.

Displays the model’s confidence score for each prediction.

Designed to be lightweight and easy to run locally or deploy online.

Tech Stack:

Python 3.9

Flask

scikit-learn

pandas, numpy

Matplotlib, Seaborn, WordCloud (for EDA)

Render (for deployment)

Folder Structure
ADS509Final/
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
├── models/
│   ├── classifier_model.pkl
│   └── text_vectorizer.pkl
├── data/
│   └── processed/news_clean.csv
├── notebooks/
│   └── ADS509_Final_Proj.ipynb
├── requirements.txt
└── README.md

Model Performance:
The model performs consistently across both classes, achieving roughly 75% accuracy.

Running Locally

Clone the repository:

git clone https://github.com/<your-username>/ADS509Final.git
cd ADS509Final


Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

cd app
python app.py


Open your browser and go to:
http://127.0.0.1:5000

Deployment Notes:

The application can be deployed for free using Render
.
Use the following start command when configuring the service:

gunicorn app.app:app


Ensure that your requirements.txt includes:

flask
scikit-learn
pandas
numpy
joblib
gunicorn

About the Author:
Created by Matt Ammirati
Master’s in Applied Data Science — University of San Diego
LinkedIn: https://www.linkedin.com/in/mattammirati/

GitHub: https://github.com/Mam