# Проект: microservices
Описание проекта: пользовательский сервис для поиска товара. 
Высоконагруженный сервис с большой частотой запросов, так как информация о 
товарах редко меняется для оптимизации запросов к базе данных, то информация о 
товарах храниться в кеше.

Общая схема работы:

1. Пользователь отправляет запрос к Django-бэкенду.
2. Django проверяет наличие данных в Redis:
   1. Если данные есть → возвращает их пользователю.
   2. Если данных нет → отправляет событие в Kafka.
3. Микросервис на FastAPI обрабатывает событие из Kafka:
   1. Извлекает данные из основного БД.
   2. Сохраняет данные в Redis.
4. Django получает обновленные данные из Redis и возвращает их пользователю.

## Как развернуть проект

## 1. Клонировать проект с GitHub
```commandline
git@github.com:Alexey-Koltsov/microservices.git
```

## 2. Перейти в директорию проекта
```commandline
cd microservices
```

## 3. Создать в корне проекта файл .env с данными 
```commandline
ENV=production
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=db
SECRET_KEY=django-insecure-@e+$(e&mcqwq!9ps%t2as(-o9^(q7h--((b-jbj=6nit7@@p0%

DEBUG=True
ALLOWED_HOSTS=127.0.0.1 localhost

REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB_NUMBER=0
REDIS_PASSWORD=my_redis_password
REDIS_USER=my_user
REDIS_USER_PASSWORD=my_user_password


ZOOKEEPER_CLIENT_PORT: 2181

KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
KAFKA_LISTENERS: PLAINTEXT://kafka:9092
KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

TOPIC=my-topic
BOOTSTRAP_SERVERS=kafka:9092
GROUP_ID=my-group
```

## 4. Поднимаем сеть контейнеров

В новом окне терминала перейти в корневую директорию проекта, где находится 
файл docker-compose.yaml, и ввести в командной строке
```commandline
docker compose -f docker-compose.yaml up --build
```

## 5. Переходим по адресу к эндпоинтам FastAPI и создаем продукты в базе данных Postgres
```commandline
http://127.0.0.1:9000/docs#/
```

## 6. Переходим по адресу к эндпоинтам DjangoAPI и запрашиваем продукты по их id
```commandline
http://127.0.0.1:8000/swagger/
```
