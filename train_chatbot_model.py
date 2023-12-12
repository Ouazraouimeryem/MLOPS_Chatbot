# -*- coding: utf-8 -*-
"""train_chatbot_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hkkxnr33Ma3Bq9SiAnWyfZsApIKs1cW2
"""

# train_chatbot_model.py

import numpy as np
import random  # Ajoutez cette ligne
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import pickle

# Charger les données prétraitées à partir du fichier pickle
with open('lemmatized_documents.pkl', 'rb') as file:
    lemmatized_documents = pickle.load(file)

with open('words.pkl', 'rb') as file:
    words = pickle.load(file)

with open('classes.pkl', 'rb') as file:
    classes = pickle.load(file)

# Créer le jeu de données d'entraînement
training = []
output_empty = [0] * len(classes)

for doc, curr_class in zip(lemmatized_documents, classes):
    bag = []
    pattern_words = doc.split()

    # Créer un vecteur de sortie vide pour le document actuel
    output_row = list(output_empty)

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # Marquer la classe (tag) correspondante comme 1 dans le vecteur de sortie
    output_row[classes.index(curr_class)] = 1

    training.append([bag, output_row])

# Mélanger les données d'entraînement
random.shuffle(training)

# Diviser les données d'entraînement en X et Y
train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])

# Créer le modèle
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compiler le modèle
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entraîner le modèle
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Sauvegarder le modèle
model.save('chatbot_model.h5')

print("Modèle créé et sauvegardé avec succès.")

# Sauvegarder le modèle au format Keras
#model.save('chatbot_model.keras')