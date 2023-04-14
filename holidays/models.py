from django.db import models


class Department(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text


class Employee(models.Model):
    name_text = models.CharField(max_length=200)
    email_text = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.email_text


class TimeOff(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField("holiday start")
    end_date = models.DateTimeField("holiday end")
    hours = models.IntegerField(default=0)

    def __str__(self):
        return self.id
