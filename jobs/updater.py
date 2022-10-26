from apscheduler.schedulers.background import BackgroundScheduler
from jobs.jobs import update_points

def start_update_points():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_points, 'interval', minutes=1) #every week in production
    scheduler.start()