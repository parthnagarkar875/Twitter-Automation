

https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39

https://medium.com/datadriveninvestor/making-a-quote-tweeting-twitter-bot-with-python-tweepy-and-heroku-69a11cd3f47e

https://medium.com/better-programming/introduction-to-apscheduler-86337f3bb4a6

The last link has finally been followed by me. It uses APScheduler.

At the end, I enabled the WORKER dyno.

Also, I defined the Twitter API keys in environment variables of Heroku.



At the end, heroku didn't work because of dyno sleeping. 

So uploaded on AWS Elastic Beanstalk instead. 
