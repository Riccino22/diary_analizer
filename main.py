from nltk.sentiment import SentimentIntensityAnalyzer

with open("diary/2023-10-21.txt") as file:
    text = file.read()

analizer = SentimentIntensityAnalyzer()