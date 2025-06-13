import redis


def get_redis_client():
    """Подключение к Redis"""
    return redis.StrictRedis(host='redis', port=6379, db=0)
