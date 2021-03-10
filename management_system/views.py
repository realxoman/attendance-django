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
    pr = date.today()
    pr2 = datetime.now()
    for course in courseslist:
        mytime = course.date_payment - timedelta(days=3)
        if mytime == pr:
            course.payment_status = True
            course.save()
    coursejalase = Jalase.objects.filter(attend = False)
    for course in coursejalase:
        mytime = course.date_jalase
        print(mytime)
    return render(request,"cron.html",{"ct": ct,"pr": pr,"courseslist": courseslist})
            