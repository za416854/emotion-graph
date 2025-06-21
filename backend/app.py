from flask import Flask, request, jsonify
from sentiment import analyze_sentiment
from neo4j_driver import create_user_sentiment

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')
    user_id = data.get('user_id', 'anonymous')

    if not text:
        return jsonify({"error": "text is required"}), 400

    sentiment_label, score = analyze_sentiment(text)
    create_user_sentiment(user_id, text, sentiment_label)

    return jsonify({
        "user_id": user_id,
        "text": text,
        "sentiment": sentiment_label,
        "confidence": round(score, 3)
    })

if __name__ == '__main__':
    app.run(debug=True)
