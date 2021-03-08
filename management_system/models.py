from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TarahiClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="ساده",verbose_name="نام")
    level = models.CharField(max_length=50,default="ساده",verbose_name="سطح")
    class Meta:
        verbose_name = 'نوع کلاس'
        verbose_name_plural = 'انواع کلاس ها'


class UserTerm(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,verbose_name="نام کاربری هنرجو")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'کلاس کاربران'
        verbose_name_plural = 'کلاس های کاربران'
