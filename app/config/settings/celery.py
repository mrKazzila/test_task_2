from os import environ

REDIS_HOST = environ['REDIS_HOST']
REDIS_PORT = environ['REDIS_PORT']

CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_SCHEDULE_TIME_MINUTES = environ['CELERY_SCHEDULE_TIME_MINUTES']
