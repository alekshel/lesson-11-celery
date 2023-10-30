## 1. Install dependencies
```
pip install -r requirements.txt
```

## 2. Run broker RabbitMQ
```
docker run -d -p 5672:5672 rabbitmq
```

## 3. Set vars in .env
```
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
```

## 4. Run worker
```
celery -A lesson_11_celery worker -l INFO

або на Windows
celery -A lesson_11_celery worker -l INFO --pool=solo
```

## 5. Run Django web server
```
py manage.py runserver
or
python manage.py runserver
```