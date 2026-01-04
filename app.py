import streamlit as st
import joblib
import numpy as np
import re
from scipy.sparse import hstack

classifier = joblib.load("models/classifier.pkl")
vectorizer = joblib.load("models/tfidf.pkl")
regressor = joblib.load("models/regressor.pkl")
KEYWORDS = joblib.load("models/keywords.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+\-*/=<> ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def keyword_features(text):
    return [text.count(k) for k in KEYWORDS]

def numeric_features(text):
    return [ len(text), sum(c.isdigit() for c in text),sum(c in "+-*/=<>" for c in text)]

def predict_problem(description,input_desc,output_desc):
    text = clean_text(description + " " + input_desc + " " + output_desc)
    tfidf_vec=vectorizer.transform([text])
    key_vec = np.array([keyword_features(text)])
    num_vec = np.array([numeric_features(text)])
    final_vec = hstack([tfidf_vec,key_vec,num_vec])

    predicted_class = classifier.predict(final_vec)[0]
    predicted_score = regressor.predict(final_vec)[0]

    return predicted_class,predicted_score


st.title("AutoJudge: Programming Problem Difficulty Predictor")
st.write("Enter the new programming description below:")
description = st.text_area("Problem Description")
input_desc = st.text_area("Input Description")
output_desc = st.text_area("Output Description")

if st.button("Predict"):
    if description and input_desc and output_desc:
        label, score= predict_problem(description, input_desc, output_desc)
        st.success(f"Predicted Difficulty Class: **{label.upper()}**")
        st.info(f"Predicted Difficulty Score: **{score} / 10**")

    else:

        st.warning("Please enter all the fields.")
