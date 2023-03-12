import os
import schedule
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

def run_cron_job():
    # Add your code here
    print('Running cron job...')

# Schedule the cron job to run once a day at 12:00 PM UTC
schedule.every().day.at('12:00').do(run_cron_job)

if __name__ == '__main__':
    app.run()
    while True:
        schedule.run_pending()
        time.sleep(1)