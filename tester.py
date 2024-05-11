import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def polarity_check(text):
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['neg']<sentiment_scores['pos']:
        print('positive')
    else:
        print('negative')
polarity_check("I like this Code. ")
polarity_check("I don't like this Code. ")

BASE_URL = "http://0.0.0.0:5050"


FEDDIT_URL = "http://0.0.0.0:8080/api/v1"
response = requests.get(f"{FEDDIT_URL}/subfeddits/",params={"skip": 0, "limit": 30},)
subfeddits = eval(str(response.json()))['subfeddits']
for subfeddit in subfeddits:
    id = subfeddit['id']
    params = {

        "subfeddit_id": id,
        "skip": 0,
        "limit": 25,
        "sort_by_score":True,
        "start_time": 1715170778,
        "end_time":1715170778,
    }
    response = requests.get(f"{BASE_URL}/comments/", params=params)
    print(response.json())