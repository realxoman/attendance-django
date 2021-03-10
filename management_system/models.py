from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField


# Create your models here.

class TarahiClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="ساده", verbose_name="نام")
    level = models.CharField(max_length=50,default="ساده", verbose_name="سطح")
    class Meta:
        verbose_name = 'نوع کلاس'
        verbose_name_plural = 'انواع کلاس ها'
    def __str__(self):
        return self.name


class UserTerm(models.Model):
    id = models.AutoField(primary_key=True)
    classname = models.ForeignKey(TarahiClass, null=True, blank=True, on_delete=models.CASCADE, verbose_name="انتخاب کلاس")
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE, verbose_name="نام کاربری هنرجو")
    date_pay = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True, verbose_name="تاریخ پرداخت")
    def __str__(self):
        return self.user.get_full_name() + " " + self.classname.name
    class Meta:
        verbose_name = 'کلاس کاربران'
        verbose_name_plural = 'کلاس های کاربران'

class Jalase(models.Model):
    name_jalase = models.IntegerField(null=True, default=1, verbose_name="شماره جلسه")
    attend = models.BooleanField(null=True, default=False, verbose_name="حضور")
    date_jalase = models.DateTimeField(null=True, verbose_name="زمان جلسه")
    userterm =  models.ForeignKey(UserTerm, null=True, blank=True, on_delete=models.CASCADE, verbose_name="انتخاب کلاس", related_name="jalasat")
    class Meta:
        verbose_name = 'جلسات'
        verbose_name_plural = 'جلسه'
    def __str__(self):
        return self.userterm.user.get_full_name() + " " + self.userterm.classname.name + " جلسه‌ی" + str(self.name_jalase)
    