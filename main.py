import nltk
import pickle
import numpy as np

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from nltk.corpus import stopwords
from TurkishStemmer import TurkishStemmer
from tensorflow.keras.models import load_model


class Classifier:
    def __init__(self):
        self.class_names = [class_name for class_name in open("Models/class_names.txt", "r").read().splitlines()]
        self.tfidf_vectorizer = pickle.load(open(f"Models/tfidf_vectorizer.pkl", "rb"))
        self.model = load_model("Models/keras_ann_v1.h5")
        self.stemmer = TurkishStemmer()
        self.regex_tokenizer = nltk.RegexpTokenizer(r"\w+")

        self.turkish_stop_words = stopwords.words('turkish')
        # appanding more turkish stop words
        with open("Models/more_turkish_stop_words.txt", "r", encoding="utf-8") as f:
            new_stop_words = f.read().splitlines()
            self.turkish_stop_words.extend(new_stop_words)

    def is_word_has_digit(self, word_string):
        for char in word_string:
            if char.isdigit():
                return True
        return False

    def process_news_text(self, news_text):
        tokenized_words = self.regex_tokenizer.tokenize(news_text)
        tokenized_words = [word.lower() for word in tokenized_words]
        tokenized_words = [word for word in tokenized_words if word not in self.turkish_stop_words]
        tokenized_words = [word for word in tokenized_words if not self.is_word_has_digit(word)]
        tokenized_words = [word for word in tokenized_words if len(word) > 2]
        tokenized_words = [self.stemmer.stem(word) for word in tokenized_words]

        return " ".join(tokenized_words)

    def get_tf_idf_of_data(self, processed_news_text):
        vector = self.tfidf_vectorizer.transform([processed_news_text])
        return vector.toarray()

    def predict_news_class(self, vectorized_news_text):
        prediction = self.model.predict(vectorized_news_text)
        class_number = np.argmax(prediction)
        class_name = self.class_names[class_number]
        probability = prediction[0][class_number]
        return class_name, probability

    def classify(self, news_text):
        processed_news_text = self.process_news_text(news_text=news_text)
        vectorized_news_text = self.get_tf_idf_of_data(processed_news_text=processed_news_text)
        class_name, probability = self.predict_news_class(vectorized_news_text)
        return class_name, probability



app = FastAPI()
classifier = Classifier()


class NewsData(BaseModel):
    NewsText: str


@app.post("/turkish-news-classifier/predict")
def predict_news(news_data: NewsData):
    class_name, probability = classifier.classify(news_data.NewsText)
    response = {"Class": class_name, "Probability": f"{float(probability):.2f}"}

    return response