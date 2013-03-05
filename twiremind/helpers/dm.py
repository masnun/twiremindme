import tweepy

## KEYS ##
TWITTER_CONSUMER_KEY = "NmeaIDlys71mSvCpNPcZg"
TWITTER_CONSUMER_SECRET = "r1ACQhBrLoEtikR7KYDPhkFjKeB4vCWmpZPbIxKGLY"
TWITTER_ACCESS_TOKEN = "1140530070-PFNTOozzAT5t33rAwZS3DJYa7S3Sb6EtLoYPESM"
TWITTER_TOKEN_SECRET = "OWwjaZs7GZYjibzPu0WZFbqjKxjiJPoGO1oiFCKOns"

def send_direct_message(screen_name, message):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api.send_direct_message(screen_name=screen_name, text=message)

