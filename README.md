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

## 3. Cоздать виртуальное окружение в сервисах Django и FastAPI

### 3.1. Перейти в директорию с Django  
```
cd /django_service/
```

### 3.2. Cоздать виртуальное окружение
Windows
```
python -m venv venv
```

LinuxmacOS

```
python3 -m venv venv
```

### 3.3. Активировать виртуальное окружение
Windows
```
source venv/Scripts/activate
```

LinuxmacOS
```
python3 -m venv venv source venvbinactivate
```

### 3.4. Обновить PIP

Windows
```
python -m pip install --upgrade pip
```

LinuxmacOS
```
python3 -m pip install --upgrade pip
```

### 3.5. Активировать виртуальное окружение
```
source venv/Scripts/activate
```
LinuxmacOS
```
source venv/bin/activate
```

### 3.6. Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

### 3.7. Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

### 3.8. В новом окне терминала перейти в директорию с FastAPI   
```
cd /fastapi_service/
```

### 3.9. Повторить действия из пунктов 3.2. - 3.7. в директории с FastAPI

## 4. Поднимаем сеть контейнеров

В новом окне терминала перейти в корневую директорию проекта, где находится 
файл docker-compose.yaml, и ввести в командной строке
```commandline
docker compose stop && docker compose -f docker-compose.yaml up --build --watch
```

## 5. В директории с FastAPI выполнить команду миграции в базу данных Postgrtes
```commandline
alembic upgrade head
```

## 6. В контейнере с Django выполнить команды миграции в базу данных и сбора статики
```commandline
python manage.py makemigrations

python manage.py migrate
```

```commandline
python manage.py collectstatic
```

## 7. Переходим по адресу к эндпоинтам FastAPI и создаем продукты в базе данных Postgres
```commandline
http://127.0.0.1:9000/docs#/
```

## 8. Переходим по адресу к эндпоинтам DjangoAPI и запрашиваем продукты по их id
```commandline
http://127.0.0.1:8000/api/swagger/
```
