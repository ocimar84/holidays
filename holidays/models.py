from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TimeOff(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField("holiday start")
    end_date = models.DateTimeField("holiday end")
    hours = models.IntegerField(default=0)
    reason = models.CharField(max_length=2000, null=True)
    status = models.CharField(max_length=200, default="pending")

    def start_date_(self):
        return self.start_date.strftime("%m/%d/%Y")

    def end_date_(self):
        return self.end_date.strftime("%m/%d/%Y")

    def __str__(self):
        return f'{self.id}'
