from textblob import TextBlob

# Sample text to analyze
text = "I love programming in Python! It's so much fun."

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment = blob.sentiment

# Output the polarity and subjectivity
print(f"Sentiment Polarity: {sentiment.polarity}")
print(f"Sentiment Subjectivity: {sentiment.subjectivity}")

# Interpret the sentiment
if sentiment.polarity > 0:
    print("The sentiment is Positive!")
elif sentiment.polarity < 0:
    print("The sentiment is Negative!")
else:
    print("The sentiment is Neutral!")