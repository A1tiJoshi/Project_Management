from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default settings module for the 'celery' program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_management.settings")

# Create an instance of the Celery class
app = Celery("project_management")

# Load task modules from all registered Django app configs
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
