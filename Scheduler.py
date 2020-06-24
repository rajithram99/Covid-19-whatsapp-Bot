from apscheduler.schedulers.blocking import BlockingScheduler
from script import display_all

sched = BlockingScheduler()

sched.add_job(display_all, 'cron', seconds=5)
sched.start()
