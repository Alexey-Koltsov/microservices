import json
import os
import redis

from adapters.logging.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger()


class RedisClientAdapter:
    """
    Адаптер для работы с клиентом Redis.
    """

    def __init__(self, host: str, port: int, db: int):
        """
        Инициализация адаптера RedisClientAdapter.

        :param host: Адрес хоста Redis.
        :param port: Порт, на котором работает Redis.
        :param db: Номер базы данных Redis.
        """
        self.host = host
        self.port = port
        self.db = db
        self.client = None

    def connect(self):
        """
        Устанавливает соединение с Redis.
        """
        try:
            self.client = redis.StrictRedis(host=self.host, port=self.port,
                                            db=self.db)
        except Exception as e:
            logger.error(f'Произошла ошибка подключения к Redis: {e}')

    def store_message(self, key: str, value: dict):
        """
        Сохраняет сообщение в Redis.

        :param key: Ключ, под которым будет сохранено сообщение.
        :param value: Сообщение, которое нужно сохранить (в формате словаря).
        """
        try:
            self.client.set(key, json.dumps(value))
        except Exception as e:
            logger.error(f'Произошла ошибка отправки сообщения в Redis: {e}')


client = RedisClientAdapter(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT')),
    db=int(os.getenv('REDIS_DB_NUMBER'))
)
