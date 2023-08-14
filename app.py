from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    mandarin_text = data.get('text', '')
    
    translator = Translator()
    translated_text = translator.translate(mandarin_text, src='zh-CN', dest='en')
    
    return jsonify({'translation': translated_text.text})

if __name__ == '__main__':
    app.run()
