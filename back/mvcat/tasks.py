from celery import shared_task

@shared_task
def firsttask(a,b):
    return a+b
