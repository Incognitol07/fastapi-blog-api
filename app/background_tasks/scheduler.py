from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.background_tasks import delete_old_notifications

scheduler = BackgroundScheduler()

def start_scheduler():
    # Add jobs to the scheduler
    scheduler.add_job(delete_old_notifications, IntervalTrigger(days=1))
    # Start the scheduler
    scheduler.start()