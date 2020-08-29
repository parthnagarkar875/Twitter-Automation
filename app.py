import tweepy
from flask import Flask
import gspread
from os import environ
import sys
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler

#Twitter API keys will be accessed from the environment variables. 
consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

#Initializing Google sheets API
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client=gspread.authorize(creds)
sheet=client.open('Final tweets').sheet1

def tweet_quote():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    tweet = sheet.row_values(1)[0]          #Fetching the first row from Google sheet
    api.update_status(status =tweet)        
    sheet.delete_row(1)                       

sched = BackgroundScheduler(daemon=True)
sched.add_job(tweet_quote,'interval', seconds=60)
sched.start()

app = Flask(__name__)
if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=environ.get('PORT'))
