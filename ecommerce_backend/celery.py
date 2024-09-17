from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_backend.settings")

app = Celery("ecommerce_backend")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "check-low-stock-every-day": {
        "task": "product.tasks.check_low_stock",
        "schedule": crontab(hour=0, minute=0),  # Runs daily at midnight
    },
}
