from django.urls import path
from .views import CronJobs,SuperPanel,logout_,login_,userPanel,ManageUsers,Manageclasses

app_name = "management_system"
urlpatterns = [
    path('', login_),
    path('mycrons/', CronJobs),
    path('mypanel/', SuperPanel),
    path('usercp/', userPanel),
    path('manageusers/', ManageUsers),
    path('manageclass/', Manageclasses),
    path('logout/', logout_)
]
