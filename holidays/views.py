from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from holidays.models import Department, Employee, TimeOff

from datetime import datetime


def create(request):
    format = '%m/%d/%Y'

    employee_id = request.POST["employee"]
    reason_text = request.POST["reason"]
    start_date = datetime.strptime(request.POST["start_date"], format)
    end_date = datetime.strptime(request.POST["end_date"], format)
    hours = (end_date - start_date).days * 8
    status_text = 'approved'

    employee = get_object_or_404(Employee, pk=employee_id)
    time_off = TimeOff(employee=employee, reason_text=reason_text, start_date=start_date,
                       end_date=end_date, hours=hours, status_text=status_text)
    time_off.save()

    return HttpResponseRedirect(reverse('index'))


def show(request):
    return HttpResponse("Hello, world.")


def index(request):
    """View function for home page of site."""

    departments = Department.objects.all().order_by('name_text')
    employees = Employee.objects.all().order_by('name_text')
    time_offs = TimeOff.objects.select_related(
        'employee').filter(status_text__exact='approved').order_by('start_date')

    context = {
        'departments': departments,
        'employees': employees,
        'time_offs': time_offs
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
