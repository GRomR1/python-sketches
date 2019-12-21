import datetime
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


def timed_job():
    cur_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Async:', cur_datetime)  # '2019-04-10 20:45:00'


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(timed_job, 'interval', seconds=1, id='timed_job')
    scheduler.start()

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

# ********* RESULTS ********* #
# Async: 2019-04-10 21:44:31
# Async: 2019-04-10 21:44:32
# Async: 2019-04-10 21:44:33
# ....
