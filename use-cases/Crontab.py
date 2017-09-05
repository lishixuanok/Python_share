import datetime
from apscheduler.schedulers.gevent import GeventScheduler


# apscheduler document
# http://apscheduler.readthedocs.io/en/latest/

def schedule():
    print('Add at %s' % datetime.datetime.now())
    scheduler = GeventScheduler()
    scheduler.add_job(hello, args=['haha'],
                      trigger='cron', hour=15, minute=11, max_instances=20, misfire_grace_time=7200)
    g = scheduler.start()
    scheduler.print_jobs()
    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass


# TODO: add your function here
def hello(from_who='Genius'):
    print('Start at %s' % datetime.datetime.now())
    print('Hello World %s' % from_who)


if __name__ == '__main__':
    schedule()
