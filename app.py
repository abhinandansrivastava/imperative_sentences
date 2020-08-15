from flask import Flask, request, jsonify
import spacy
import re
from tqdm import tqdm
from utils import word_tag_pairs
from utils import extract_email_msg
from utils import imperative_sentences
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return jsonify({"response":imperative_sentences(word_tag_pairs(nlp('Check this out')))})
    elif request.method == 'POST':
        req_Json = request.json
        name = req_Json['name']
        # return jsonify({"response": get_tokens(name)})
        return jsonify({"response":imperative_sentences(word_tag_pairs(nlp(name)))})


if __name__ == "__main__":
    app.run(debug = True,port = 8080)
