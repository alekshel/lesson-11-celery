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
PHONE_FOR_SMS=
```

## 4. Run worker
```
celery -A lesson_11_celery worker -l INFO
```

## 5. Run Django web server
```
py manage.py runserver
or
python manage.py runserver
```