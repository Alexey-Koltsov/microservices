import asyncio
from adapters.kafka_app.kafka_utils import KafkaConsumerAdapter
from adapters.redis_app.redis_utils import RedisClientAdapter

client = RedisClientAdapter(host='redis', port=6379, db=0)

# Подключение к Redis
client.connect()


# Настройка консюмера
consumer = KafkaConsumerAdapter(
    'my-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
)


async def consume():
    await asyncio.sleep(60)
    await consumer.start()
    await consumer.get_messages(client=client)
