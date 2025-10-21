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

## Live Demo
[View the App on Render](https://ads509-final-news-bias.onrender.com)


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

How to Run this Locally: 

# Clone repo and set up environment
git clone https://github.com/Mammaritati15/ads509-final-news-bias.git
cd ads509-final-news-bias
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/app.py


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