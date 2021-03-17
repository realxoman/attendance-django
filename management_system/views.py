from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Jalase,UserTerm
from datetime import date, timedelta
from django.urls import reverse
from ippanel import *
from .forms import SignUpForm

# Create your views here.

def signup(request):
    payam = "شما در حال ساخت کاربر جدید هستید."
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.phoneNumber = form.cleaned_data.get('phoneNumber')
            user.save()
            payam = "کاربر ساخته شد."
            render(request, 'register.html', {'form': form , 'payam' : payam})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form , 'payam' : payam})

def login_(request):
    error=False
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if request.user.is_staff:
                return HttpResponseRedirect("/mypanel/")
            else:
                return HttpResponseRedirect("/usercp/")
        elif user is none:
            error = True
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect("/mypanel/")
        else:
            return HttpResponseRedirect("/usercp/")
    else:
        return render(request, "home.html", {"error":error})

    
def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")

def userPanel(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect("/mypanel/")
        else:
            return render(request,"userpanel.html")
    return HttpResponseRedirect("/")

def SuperPanel(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request,"superpanel.html")
        else:
            return HttpResponseRedirect("/usercp/")
    else:
        return HttpResponseRedirect("/")
    
def ManageUsers(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request,"manageusers.html")
        else:
            return HttpResponseRedirect("/usercp/")
    else:
        return HttpResponseRedirect("/")

def Manageclasses(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request,"manageclasses.html")
        else:
            return HttpResponseRedirect("/usercp/")
    else:
        return HttpResponseRedirect("/")

def CronJobs(request):
    courseslist = UserTerm.objects.filter(payment_status = False)
    ct = False
    pr = date.today()
    api_key = "B9onqAUmrWEmFNL2zoZ-IYzUYFzsJaTLD8Rvxctsqw0="
    sms = Client(api_key)
    for course in courseslist:
        mytime = course.date_payment - timedelta(days=3)
        if mytime == pr:
            sms_message = "سلام\n" + course.user.get_full_name() + " عزیز،\n" + "سر رسید شهریه شما فرا رسیده است.\n لطفا جهت پرداخت آن اقدام نمایید.\n آموزشگاه طراحی چهره و سیاه قلم چهره پردازان"
            bulk_id = sms.send("+981000500030500", ["+989921658994"], sms_message)
            print(bulk_id)
    coursejalase = Jalase.objects.filter(attend = False)
    for course in coursejalase:
        mytime = course.date_jalase
        if mytime.date() < pr:
            course.attend = True
            course.save()
    return render(request,"cron.html",{"ct": ct,"pr": pr,"courseslist": courseslist})
