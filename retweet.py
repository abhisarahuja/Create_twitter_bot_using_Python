import tweepy
import time

api_key = "wnpbPQmFvjgSm8Sd1shbrLziU"
api_secret = "OnhU4EtbspdtIPuGJjIpwSgcRmOMPC4U4giYZxi3FIoS2kPglv"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAFKAkwEAAAAAGSkxdEkbpT0iGc7z9nC3MI2uP6E%3Dnagm2G9KDusq7lAJvlQJuBKfjf8zO3OdT4ExFg4437KRElyOvy"
access_token = "1608030220967358464-PgUwbaZqrKgI85DhiLwa8w9ZZdfIWs"
access_token_secret = "lnVafMZUbSHwyr7k7Sy2QdTtuiOXwDc9Wd3lwQnarqu9i"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        
        try:
            client.retweet(tweet.id)
        
        except Exception as error:
            print(error)

stream = MyStream(bearer_token = bearer_token)

rule = tweepy.StreamRule("(Virat Kohli)(-is:retweet -is:reply)" )

stream.add_rules(rule)

stream.filter()