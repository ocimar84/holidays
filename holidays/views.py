from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from holidays.models import Department, TimeOff

from datetime import datetime


def create(request):
    format = '%m/%d/%Y'

    department_id = request.POST["department"]
    reason = request.POST["reason"]
    start_date = datetime.strptime(request.POST["start_date"], format)
    end_date = datetime.strptime(request.POST["end_date"], format)
    hours = (end_date - start_date).days * 8
    status = 'requested'

    if end_date < start_date:
        return HttpResponse("The dates are invalid.", status=400)
    
    if start_date < datetime.now():
        return HttpResponse("The start date is invalid.", status=400)

    user = request.user
    department = get_object_or_404(Department, pk=department_id)
    time_off = TimeOff(user=user, department=department, reason=reason, start_date=start_date,
                       end_date=end_date, hours=hours, status=status)
    time_off.save()

    return HttpResponseRedirect(reverse('profile'))


def show(request):
    return HttpResponse("Hello, world.")

def profile(request):
    """View function for profile page of site."""

    departments = Department.objects.all().order_by('name')
    if request.user.is_superuser:
        time_offs = TimeOff.objects.select_related('user').filter(status__in=['requested', 'approved']).order_by('start_date')
    else:
        time_offs = TimeOff.objects.select_related('user').filter(user__exact=request.user.id, status__in=['requested', 'approved']).order_by('start_date')

    context = {
        'departments': departments,
        'time_offs': time_offs
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profile.html', context=context)

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')
