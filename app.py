from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.utils import simple_preprocess
import string

app = Flask(__name__)

# Download the necessary resources
nltk.download('punkt')

# Load the spaCy model (if needed)
# nlp = spacy.load('en_core_web_sm')

def calculate_score(incorrect_words):
    base_score = 100.0  # Starting with a base score of 100%
    penalty = len(incorrect_words) * 10.0  # Deducting 10% for each incorrect word
    score = max(base_score - penalty, 0.0)  # Ensure the score is not negative
    return score

@app.route('/calculate_score', methods=['POST'])
def calculate_score_api():
    try:
        data = request.get_json()
        incorrect_words = data.get('incorrect_words')
        score = calculate_score(incorrect_words)
        response = {'score': score}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
