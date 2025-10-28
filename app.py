from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "✅ CyberShield AI Backend is Running!"

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    url = data.get('url', '').lower()

    suspicious_words = ['login', 'verify', 'update', 'password', 'free', 'bonus']
    is_phish = any(word in url for word in suspicious_words)

    return jsonify({'url': url, 'is_phish': is_phish})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
