import tweepy

consumer_key = "2dTGQgi9FqZLfHW5eBkVSgrMx"
consumer_secret = "tFCw2ToP95D9QdQ3aJqt0IodaAhKz3CEssCjAOe7Dl3qF7I88c"
access_token = "747300639563087874-XiAlvP7mrLx9NZsnpw7F5XyDqpHSmf8"
access_secret = "ktcsBxDfvwv5iqiOOq64jH8OHRSvD7nqw4vQPWgXWdW5v"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
places = api.geo_search(query="USA", granularity="country")
place_id = places[0].id

print("OK")
tweets = api.search(q="place:%s" % place_id, count=1)
for tweet in tweets:
    print(tweet.text + " \n\n " +  tweet.place.name if tweet.place else "Undefined place")