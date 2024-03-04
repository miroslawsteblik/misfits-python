import tweepy
import twitter_config

bt = twitter_config.BEARER_TOKEN

# Authenticate with OAuth 2.0 Bearer Token (App only)
client = tweepy.Client(bearer_token=bt)

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)