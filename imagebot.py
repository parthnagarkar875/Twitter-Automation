import tweepy

consumer_key = 'HRHs5HlGETvQ6xrKfNbEyji1L'
consumer_secret_key = 'i9KUBqRYJ7hmsrloe3pHxd9fxKZrBJmeZsKnYMkrblE46J2E2v'
access_token = '1002268050513575936-pMYrBqAxUvCQkrR9p5wvuuA15TC1XK'
access_token_secret = 'MbdJsSft3P2gy6cM98musrup8Xxo11JF74ZwLKsyv3dNr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)    
api = tweepy.API(auth,wait_on_rate_limit=True)


media = api.media_upload("mach_face.jpeg")

tweet = "Test. Ignore this tweet. "

post_result = api.update_status(status=tweet, media_ids=[media.media_id])