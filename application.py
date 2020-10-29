import tweepy
from flask import Flask
import gspread
from os import environ
import credentials
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'client_secret.json')

#Initializing Google sheets API
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name(my_file, scope)
client=gspread.authorize(creds)
sheet=client.open('Final tweets').sheet1

def tweet_quote():
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret_key)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)    
    api = tweepy.API(auth,wait_on_rate_limit=True)

    tweet = sheet.row_values(1)[0]          #Fetching the first row from Google sheet
    api.update_status(status =tweet)        
    sheet.delete_row(1)                       

sched = BackgroundScheduler(daemon=True)
sched.add_job(tweet_quote,'interval', hours=3)
sched.start()

application = app = Flask(__name__)

@app.route('/')
def home():
    return "Doing..."

if __name__ == "__main__":    
    app.run(debug=True)

