#Task 4 Sentiment Analysis using Textblob

from textblob import TextBlob
import pandas as pd

data = {
    'text': [
        "I love this product! It’s amazing and works well.",
        "Worst service ever. I’m very disappointed.",
        "The product is okay, nothing special.",
        "Absolutely fantastic experience! Highly recommended.",
        "Not worth the price at all.",
        "Pretty average, not bad.",
        "Terrible quality. Will not buy again.",
        "Great value for the money!"
    ]
}

df = pd.DataFrame(data)

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return pd.Series([polarity, sentiment])

df[['Polarity', 'Sentiment']] = df['text'].apply(get_sentiment)

print(df)
