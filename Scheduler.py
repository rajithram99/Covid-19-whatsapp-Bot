from script import *
import schedule
import time

# run the function job() every 2 seconds
schedule.every(2).seconds.do(func())

while True:
    schedule.run_pending()
    time.sleep(1)
