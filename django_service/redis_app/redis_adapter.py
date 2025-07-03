import os
import redis
from dotenv import load_dotenv

load_dotenv()

client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT')),
    db=int(os.getenv('REDIS_DB_NUMBER'))
)
