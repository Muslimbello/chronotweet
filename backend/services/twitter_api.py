# In services/twitter_api.py
import os
import tweepy
from ..core.models import UserProfile


class TwitterAPIClient:
    def __init__(self, access_token):
        self.client = tweepy.Client(
            bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=access_token,
        )
