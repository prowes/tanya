import tweepy
import credentials  # please create your own

#NB: you need to have Elevated twitter access to be able to post media
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

api = tweepy.API(auth)
filename = "/home/ec2-user/tanya/pic.jfif"
media = api.media_upload(filename)
api.update_status(status='', media_ids=[media.media_id])

