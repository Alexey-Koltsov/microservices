from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaError
import asyncio
import json
import redis
from attr import asdict

from adapters.database.database import get_async_session
from adapters.database.repositories.product_repository import ProductRepository


# Подключение к Redis
client = redis.StrictRedis(host='redis', port=6379, db=0)


async def consume():
    # Настройка консюмера
    consumer = AIOKafkaConsumer(
        'my-topic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    await asyncio.sleep(30)
    await consumer.start()
    try:
        while True:
            async for message in consumer:
                if not message:
                    continue
                else:
                    async for session in get_async_session():
                        product_id = message.value
                        product_repository = ProductRepository(session=session)
                        result = await product_repository.get_product(
                            product_id=product_id)
                        if not result:
                            # TODO: сделать обработку исключения, если товар не найден
                            print('Product not found')
                        # Запись данных
                        client.set(product_id, json.dumps(asdict(result),
                                                          ensure_ascii=False))
    except KafkaError as e:
        print(e)
    finally:
        await consumer.stop()
