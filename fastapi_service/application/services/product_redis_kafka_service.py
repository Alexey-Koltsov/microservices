import os

from adapters.kafka_app.kafka_consumer import consumer
from adapters.redis_app.redis_utils import client
from dotenv import load_dotenv

load_dotenv()

client.connect()


async def consume():
    """
    Асинхронная функция для запуска потребителя Kafka и получения сообщений.
    """
    await consumer.start()
    await consumer.get_messages(client=client)
