from django.contrib import admin

from .models import Department, Employee, TimeOff

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(TimeOff)
