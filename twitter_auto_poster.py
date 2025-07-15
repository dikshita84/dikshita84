import os
import random
import tweepy

# Grab API credentials from environment variables
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise RuntimeError('Twitter API credentials are not fully set in environment variables')

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

PYTHON_TIPS = [
    "List comprehensions can simplify loops in Python.",
    "Generators help save memory when dealing with large datasets.",
    "Use virtual environments to manage project dependencies.",
]

PINE_TIPS = [
    "The `plot` function is great for visualizing data in Pine Script.",
    "`strategy.entry` helps you create trading signals.",
    "Version 5 of Pine Script adds many quality-of-life improvements.",
]

def create_tweet():
    """Return a random tweet about Python or Pine Script."""
    if random.random() < 0.5:
        tip = random.choice(PYTHON_TIPS)
        return f"Python tip: {tip}"
    else:
        tip = random.choice(PINE_TIPS)
        return f"Pine Script tip: {tip}"

def main():
    tweet = create_tweet()
    api.update_status(status=tweet)
    print(f"Tweeted: {tweet}")

if __name__ == "__main__":
    main()
