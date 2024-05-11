"""
This module contains a script for performing polarity checks on text
using the VADER sentiment analyzer
and
making requests to the specified API endpoints for testing once the services are up.
"""

import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon if not already available
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def polarity_check(text):
    """
    Function docstring: Perform a polarity check on the given text.
    :param text: The text to perform the polarity check on.
    """
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['neg'] < sentiment_scores['pos']:
        print('positive')
    else:
        print('negative')

# Perform polarity checks on example texts
polarity_check("I like this Code. ")
polarity_check("I don't like this Code. ")

# Define base and Feddit API URLs
BASE_URL = "http://0.0.0.0:5050"
FEDDIT_URL = "http://0.0.0.0:8080/api/v1"

# Make a request to retrieve subfeddits
response = requests.get(f"{FEDDIT_URL}/subfeddits/", params={"skip": 0, "limit": 30})
subfeddits = eval(str(response.json()))['subfeddits']

# Iterate over subfeddits and make requests to retrieve comments
for subfeddit in subfeddits:
    sf_id = subfeddit['id']
    params = {
        "subfeddit_id": sf_id,
        "skip": 0,
        "limit": 25,
        "sort_by_score": True,
        "start_time": 1715170778,
        "end_time": 1715170778,
    }
    response = requests.get(f"{BASE_URL}/comments/", params=params)
    print(response.json())
