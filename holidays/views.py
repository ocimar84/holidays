from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from holidays.models import Department, TimeOff

from datetime import datetime


def create(request):
    format = '%m/%d/%Y'

    error = False
    message = ""
    message_type = "alert"

    try:
        department_id = request.POST["department"]
        reason = request.POST["reason"]
        start_date = datetime.strptime(request.POST["start_date"], format)
        end_date = datetime.strptime(request.POST["end_date"], format)
        hours = (end_date - start_date).days * 8
        status = 'requested'
    except:
        error = True
        message = "Data are invalid"    

    if end_date < start_date:
        error = True
        message = "The dates are invalid"
    
    if start_date < datetime.now():
        error = True
        message = "The start date is invalid"

    if error == False:
        user = request.user
        department = get_object_or_404(Department, pk=department_id)
        time_off = TimeOff(user=user, department=department, reason=reason, start_date=start_date,
                        end_date=end_date, hours=hours, status=status)
        time_off.save()
        message_type = 'success'
        message = "You timeoff was created"

    return HttpResponseRedirect(reverse('profile') + "?mt=%s&mc=%s" % (message_type, message))

def destroy(request, id):
    error = False
    message = ""
    message_type = "alert"

    user = request.user

    try:
        time_off = get_object_or_404(TimeOff, pk=id)
    except:
        error = True
        message = "Data are invalid"

    if time_off.user_id != user.id:
        error = True
        message = "This timeoff is not your"

    if error == False:
        time_off.delete()
        message_type = 'success'
        message = "You timeoff was deleted"

    return HttpResponseRedirect(reverse('profile') + "?mt=%s&mc=%s" % (message_type, message))

def profile(request):
    """View function for profile page of site."""

    message_type = request.GET.get("mt")
    message_content = request.GET.get("mc")

    departments = Department.objects.all().order_by('name')
    if request.user.is_superuser:
        time_offs = TimeOff.objects.select_related('user').filter(status__in=['requested', 'approved']).order_by('start_date')
    else:
        time_offs = TimeOff.objects.select_related('user').filter(user__exact=request.user.id, status__in=['requested', 'approved']).order_by('start_date')

    context = {
        'departments': departments,
        'time_offs': time_offs,
        'message_type': message_type,
        'message_content': message_content,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profile.html', context=context)

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')
