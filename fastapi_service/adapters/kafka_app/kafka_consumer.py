import asyncio
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaError
import json
from attr import asdict

from adapters.database.database import get_async_session
from adapters.database.repositories.product_repository import ProductRepository
from adapters.redis_app.redis_utils import RedisClientAdapter
from application.logging.logger import get_logger

logger = get_logger()


class KafkaConsumerAdapter:
    def __init__(self, topic, bootstrap_servers, auto_offset_reset,
                 enable_auto_commit, group_id):
        self.consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit=enable_auto_commit,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        )

    async def start(self):
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()

    async def get_messages(self, client: RedisClientAdapter):
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
                            # result = {'error': 'Product not found'}
                            logger.info('Отправляем в Redis продукт: '
                                        '{}')
                            client.store_message(product_id, dict({}))
                        # Запись данных в Redis
                        else:
                            logger.info('Отправляем в Redis продукт: '
                                        f'{result}')
                            client.store_message(product_id,
                                                 asdict(result))
                # await asyncio.sleep(1)
        except KafkaError as e:
            logger.error(f'Произошла ошибка обработки Kafka: {e}')
