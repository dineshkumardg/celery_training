from celery import Celery
from celery.schedules import crontab

app = Celery('tasks',
             backend='redis://redis:6379/2',
             broker='redis://redis:6379/2')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    print('the sender %s $$$$$$' %sender)
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=11, minute=30, day_of_week=2),
        test.s('Happy Tuesdays!'),
    )

@app.task
def add(x, y):
   return x + y

@app.task
def test(arg):
    print(arg)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'

