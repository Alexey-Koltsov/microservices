import os
import logging
import time

from django.http import Http404, JsonResponse
from dotenv import load_dotenv
from drf_yasg.utils import swagger_auto_schema
import json
import redis
from rest_framework.decorators import api_view

from kafka_app.kafka_producer import producer
from redis_app.redis_adapter import client

load_dotenv()

logger = logging.getLogger(__name__)


@swagger_auto_schema(method='get', responses={200: 'ОК'})
@api_view(['GET'])
def get_product(request, product_id):
    """Получить продукт по его id."""
    if request.method == 'GET':
        value = client.get(product_id)
        logger.info(f'По ключу {product_id} получили значение {value}')
        if not value:
            producer.send('my-topic', product_id)
            producer.flush()
            logger.info(f'Отправили ключ {product_id} в Kafka')

            time.sleep(2)

            value = client.get(product_id)
            logger.info(f'Повторно по ключу {product_id} получили значение'
                        f' {value}')
        if value and isinstance(value, bytes):
            value = value.decode('utf-8')
        else:
            return JsonResponse({'detail': 'Product not found'}, status=404)
        json_data = json.loads(value)
        if not json_data:
            return JsonResponse({'detail': 'Product not found'}, status=404)
        logger.info(f'Получили данные из Redis {json_data}')
        return JsonResponse({'product': json_data})
