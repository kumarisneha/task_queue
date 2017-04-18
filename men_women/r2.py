from redis import Redis
from rq import Queue

q1 = Queue('low',connection=Redis())

q2 = Queue('high',connection=Redis())
