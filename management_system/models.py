from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from datetime import datetime
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, blank=True, verbose_name="نام")
    lname = models.CharField(max_length=50, blank=True, verbose_name=" نام خانوادگی")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="توضیحات کاربر")
    class Meta:
        verbose_name = 'پروفایل کاربر'
        verbose_name_plural = 'پروفایل کاربران'
    def save(self, *args, **kwargs):
        user = User.objects.get(id=self.user.id)
        user.first_name = self.fname
        user.last_name = self.lname
        user.save()
    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_delete, sender=Profile)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()

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
    payment_status = models.BooleanField(null=True,default=False, verbose_name="پرداخت انجام شده است؟")
    date_payment = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True ,verbose_name="تاریخ سر رسید")
    date_payment2 = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True, verbose_name="تاریخ پرداخت")

    def __str__(self):
        return self.user.get_full_name() + " " + self.classname.name
    class Meta:
        verbose_name = 'کلاس کاربران'
        verbose_name_plural = 'کلاس های کاربران'

class Jalase(models.Model):
    name_jalase = models.IntegerField(null=True, default=1, verbose_name="شماره جلسه")
    attend = models.BooleanField(null=True,default=False, verbose_name="برگزار شده؟")
    date_jalase = models.DateTimeField(null=True,default=datetime.now() ,verbose_name="زمان جلسه")
    userterm =  models.ForeignKey(UserTerm, null=True, blank=True, on_delete=models.CASCADE, verbose_name="انتخاب کلاس", related_name="jalasat")
    class Meta:
        verbose_name = 'جلسه'
        verbose_name_plural = 'جلسات'
    def __str__(self):
        return self.userterm.user.get_full_name() + " " + self.userterm.classname.name + " جلسه‌ی" + str(self.name_jalase)

