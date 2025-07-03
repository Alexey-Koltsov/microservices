import json
import os

from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaError
from attr import asdict

from adapters.database.settings import get_async_session
from adapters.database.repositories.product_repository import ProductRepository
from adapters.redis_app.redis_utils import RedisClientAdapter
from adapters.logging.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger()


class KafkaConsumerAdapter:
    """
    Адаптер для потребителя Kafka, который получает сообщения из указанной темы
    и обрабатывает их, отправляя результаты в Redis.

    Attributes:
        consumer (AIOKafkaConsumer): Потребитель Kafka для чтения сообщений.
    """

    def __init__(self, topic, bootstrap_servers, auto_offset_reset,
                 enable_auto_commit, group_id):
        """
        Инициализирует KafkaConsumerAdapter.

        Args:
            topic (str): Название темы Kafka для подписки.
            bootstrap_servers (str): Адреса серверов Kafka.
            auto_offset_reset (str): Политика сброса смещения.
            enable_auto_commit (bool): Флаг подтверждения смещения.
            group_id (str): Идентификатор группы потребителей.
        """
        self.consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit=enable_auto_commit,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        )

    async def start(self):
        """Запускает потребителя Kafka, чтобы начать получать сообщения."""
        await self.consumer.start()

    async def stop(self):
        """Останавливает потребителя Kafka."""
        await self.consumer.stop()

    async def get_messages(self, client: RedisClientAdapter):
        """
        Получает сообщения из Kafka и обрабатывает их.

        Args:
            client (RedisClientAdapter): Адаптер для работы с Redis.
        """
        try:
            async for message in self.consumer:
                if not message:
                    continue
                else:
                    async for session in get_async_session():
                        product_id = message.value
                        product_repository = ProductRepository(session=session)
                        result = await product_repository.get_product(
                            product_id=product_id)
                        logger.info(f'Получен продукт: {result}')
                        if not result:
                            logger.info('Отправляем в Redis продукт: {}')
                            client.store_message(product_id, dict({}))
                        else:
                            logger.info('Отправляем в Redis продукт: {result}')
                            client.store_message(product_id, asdict(result))
        except KafkaError as e:
            logger.error(f'Произошла ошибка обработки Kafka: {e}')


consumer = KafkaConsumerAdapter(
    os.getenv('TOPIC'),
    bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=os.getenv('GROUP_ID'),
)
