import tweepy
from flask import Flask
import gspread
from os import environ
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler

#Twitter API keys will be accessed from the environment variables. 
consumer_key = 'zJVhlGfigW1xeDHK3y16lCnQZ'
consumer_secret_key = 'NJPC86WrRlI6nojBzYHr1ZjxWQBTPiZ8lXYJeZhbESuwSIsWSE'
access_token = '1277604089535160320-nzQwbJncqXQEaWzq23PUR4gN5N6kc1'
access_token_secret = 'Ez48seBANENmIk5h8mqHAPGcaOL1YBJcZYIWeM9xMOruc'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'client_secret.json')

#Initializing Google sheets API
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name(my_file, scope)
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
sched.add_job(tweet_quote,'interval', hours=3)
sched.start()

application = app = Flask(__name__)

@app.route('/')
def home():
    return "Doing..."

if __name__ == "__main__":    
    app.run(debug=True)

