# Chatbot-MLOps
Ce repository contient les ressources nécessaires pour déployer un modèle de chatbot dans un environnement de production.
# Chatbot Flask Application

This is a simple chatbot application built using Flask, Keras, NLTK, and other libraries.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Imanetoumouh/Chatbot-MLOps.git
    cd Chatbot-MLOps
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python chatbot_flask.py
    ```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

- Access the chatbot interface by visiting [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.
- Enter a message in the input field and click "Send" to interact with the chatbot.

## Project Structure

- `chatbot_flask.py`: Main Flask application file.
- `chatbot_model.h5`: Trained chatbot model.
- `classes.pkl`: Pickle file containing classes.
- `intents.json`: JSON file containing intents for the chatbot.
- `preprocess_data.py`: Module for data preprocessing.
- `train_chatbot_model.py`: Script to train the chatbot model.
- `words.pkl`: Pickle file containing words.
- `lemmatized_documment.pkl`: Pickle file containing lemmatized documents.
- `templates/index.html`: HTML template for the chatbot interface.
