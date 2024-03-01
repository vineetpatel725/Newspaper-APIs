from celery import Celery

from config import global_config

broker_url: str = (
    f"redis://{global_config.get('REDIS', 'USERNAME')}:{global_config.get('REDIS', 'PASSWORD')}"
    f"@{global_config.get('REDIS', 'HOST')}:{global_config.getint('REDIS', 'PORT')}/"
    f"{global_config.getint('REDIS', 'BROKER_DB')}"
)

app: Celery = Celery("newspapers", broker=broker_url, include=['app.services'])


def store_newspaper_details():
    from app.services import store_top_headlines
    store_top_headlines()


app.conf.beat_schedule = {
    'newspapers-add-task': {
        'task': 'newspapers.store_newspaper_details',
        'schedule': 10.0
    },
}