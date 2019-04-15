"""
Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, 
either just once or periodically.

https://apscheduler.readthedocs.io/en/3.0/
"""

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=1)
def timed_job():
    cur_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(cur_datetime)  # '2019-04-10 20:45:00'

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
    
sched.start()
