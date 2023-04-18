from django.shortcuts import render

from django.http import HttpResponse

from holidays.models import Department, Employee, TimeOff


def show(request):
    return HttpResponse("Hello, world.")


def index(request):
    """View function for home page of site."""

    departments = Department.objects.all().order_by('name_text').values()
    employees = Employee.objects.all().order_by('name_text').values()
    time_offs = TimeOff.objects.all().order_by('start_date').values()
    # time_offs = TimeOff.objects.filter(status__exact='approved')

    context = {
        'departments': departments,
        'employees': employees,
        'time_offs': time_offs
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
