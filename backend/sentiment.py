from transformers import pipeline

# 初始化模型（第一次會自動下載）
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    label = result[0]['label']  # 'POSITIVE' / 'NEGATIVE'
    score = result[0]['score']
    return label, score
