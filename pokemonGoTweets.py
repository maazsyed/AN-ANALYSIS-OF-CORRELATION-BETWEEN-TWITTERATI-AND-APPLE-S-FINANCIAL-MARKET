import tweepy

ckey = ""
csecret = ""
atoken = ""
asecret = ""

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret, 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

cricTweet = tweepy.Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").items(10)

# for tweet in cricTweet:
#    # print (tweet.created_at, tweet.text, tweet.lang)
#    print (1)

for tweet in tweepy.Cursor(api.search, q=('"good book"'), since='2014-09-16', until='2014-09-17').items(5):
   print (1)