FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD ["gunicorn", "ecommerce_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
