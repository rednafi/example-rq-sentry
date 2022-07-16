import random

import rq

from app.connection import get_redis_client
from app.tasks import schedule

if __name__ == "__main__":
    while True:
        q = rq.Queue("default", connection=get_redis_client())
        schedule(q, random.randint(1, 100), random.randint(1001, 2000))
