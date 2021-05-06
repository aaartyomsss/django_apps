from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


def return_datetime():
    now = timezone.now()
    return now + datetime.timedelta(days=1)


class Todo(models.Model):
    todo_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_to = models.DateField(default=return_datetime)
    user = models.ForeignKey(User, on_delete=models.CASCADE)