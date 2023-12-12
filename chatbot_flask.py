# -*- coding: utf-8 -*-
"""chatbot_flask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dZTbKAuYrgwJO19GYCi5f32mMmhQxEGP
"""

import json
import random
from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer

# Import preprocessing functions from preprocessing.py
from preprocess_data import bow

app = Flask(__name__)

def load_chatbot_model(model_path='chatbot_model.h5', words_path='words.pkl', classes_path='classes.pkl'):
    model = load_model(model_path)
    words = pickle.load(open(words_path, 'rb'))
    classes = pickle.load(open(classes_path, 'rb'))
    return model, words, classes

def predict_class(sentence, model, words, classes, lemmatizer):
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    if not results:
        return []  # No intent found

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    return return_list

def get_response(intents_json, intent):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == intent:
            return random.choice(i['responses'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    global model, words, classes, intents_json, lemmatizer
    user_input = request.form['user_input']
    intents = predict_class(user_input, model, words, classes, lemmatizer)
    if intents:
        intent = intents[0]['intent']
        response = get_response(intents_json, intent)
        return jsonify({'response': response})
    else:
        return jsonify({'response': "I'm sorry, I didn't understand that."})

if __name__ == "__main__":
    model, words, classes = load_chatbot_model('chatbot_model.h5', 'words.pkl', 'classes.pkl')
    intents_json = json.loads(open('intents.json').read())
    lemmatizer = WordNetLemmatizer()
    app.run(debug=True, port=5000)
    