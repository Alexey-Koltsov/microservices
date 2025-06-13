from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
import json
import redis

from kafka_app.kafka_utils import producer

# Подключение к Redis
client = redis.StrictRedis(host='redis', port=6379, db=0)


@swagger_auto_schema(method='get', responses={200: "ОК"})
@api_view(['GET'])
def get_product(request, product_id):
    if request.method == "GET":
        # Получение значения по ключу
        value = client.get(product_id)
        if value:
            if isinstance(value, bytes):
                value = value.decode('utf-8')
            json_data = json.loads(value)
            return JsonResponse({"product": json_data})
        else:
            producer.send('my-topic', product_id)
            producer.flush()
            print("Отправлено")
        return JsonResponse({"product": "None"})
