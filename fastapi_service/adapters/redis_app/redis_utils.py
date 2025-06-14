import json
import redis

from application.logging.logger import get_logger

logger = get_logger()


class RedisClientAdapter:
    def __init__(self, host: str, port: int, db: int):
        self.host = host
        self.port = port
        self.db = db
        self.client = None

    def connect(self):
        try:
            self.client = redis.StrictRedis(host=self.host, port=self.port,
                                            db=self.db)
        except Exception as e:
            logger.error(f'Произошла ошибка подключения к Redis: {e}')

    def store_message(self, key: str, value: dict):
        try:
            self.client.set(key, json.dumps(value))
        except Exception as e:
            logger.error(f'Произошла ошибка отправки сообщения в Redis: {e}')
