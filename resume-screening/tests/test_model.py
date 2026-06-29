import os

import joblib


def test_resume_model_exists():
    assert os.path.exists("model/resume_model.pkl")


def test_tfidf_exists():
    assert os.path.exists("model/tfidf.pkl")


def test_model_load():
    model = joblib.load("model/resume_model.pkl")
    assert model is not None


def test_tfidf_load():
    vectorizer = joblib.load("model/tfidf.pkl")
    assert vectorizer is not None
