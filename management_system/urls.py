from django.urls import path
from .views import Home,CronJobs

app_name = "management_system"
urlpatterns = [
    path('', Home),
    path('mycrons/', CronJobs)
]
