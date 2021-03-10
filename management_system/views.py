from django.db.models.deletion import SET_NULL
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Jalase,UserTerm
from datetime import date,datetime, timedelta
from django.urls import reverse
# Create your views here.

def Home(request):
    return render(request,"home.html")

def CronJobs(request):
    courseslist = UserTerm.objects.filter(payment_status = False)
    ct = False
    pr = date.today
    for course in courseslist:
        if ((course.date_payment - timedelta(days=3)) == date.today):
            course.payment_status = True
            ct = True
            course.save()
    coursejalase = Jalase.objects.filter(attend = False)
    return render(request,"cron.html",{"ct": ct,"pr": pr,"courseslist": courseslist})
            