import tweepy
from flask import Flask
import gspread
from os import environ
import os
import credentials
import sys
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler

#grabs the path for authentication keys for google sheets API from the client_secret.json file.  
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'client_secret.json')

#Initializing Google sheets API
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name(my_file, scope)
client=gspread.authorize(creds)
sheet=client.open('Final tweets').sheet1

def tweet_quote():
    #This function fetches the top tweet from the google sheet, posts it on twitter and then deletes it from the sheet. 
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret_key)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    tweet = sheet.row_values(1)[0]          #Fetching the first row from Google sheet
    api.update_status(status =tweet)        
    sheet.delete_row(1)                       

#Initializing the scheduler. 
sched = BackgroundScheduler(daemon=True)
sched.add_job(tweet_quote,'interval', hours=5)
sched.start()

app = Flask(__name__)

@app.route('/')
def home():
    return "Doing..."

if __name__ == "__main__":    
    app.run(host='0.0.0.0',port=8080)

