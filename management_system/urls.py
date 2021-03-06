from django.urls import path
from .views import CronJobs,SuperPanel,logout_,login_,userPanel,ManageUsers,Manageclasses,signup,Userclasscp,Userclass_single

app_name = "management_system"
urlpatterns = [
    path('', login_),
    path('mycrons/', CronJobs, name="Cronjobs"),
    path('mypanel/', SuperPanel , name="SuperPanel"),
    path('usercp/', userPanel , name="userPanel"),
    path('manageusers/', ManageUsers, name="ManageUsers"),
    path('manageclass/', Manageclasses, name="ManageClasses"),
    path('logout/', logout_, name="logout_"),
    path('manageusers/adduser/', signup, name="signup"),
    path('usercp/userclasses/', Userclasscp, name="Userclasscp"),
    path('usercp/userclasses/<slug:slug>/', Userclass_single, name="Userclass_single"),
]
