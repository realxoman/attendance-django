from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from datetime import datetime
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=11,null=True, blank=True, verbose_name="شماره تلفن همراه (بدون صفر ابتدایی)")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="توضیحات کاربر")
    class Meta:
        verbose_name = 'پروفایل کاربر'
        verbose_name_plural = 'پروفایل کاربر'
    def __str__(self):
        return self.user.username
        
@receiver(post_delete, sender=Profile)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()    
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class TarahiClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="ساده", verbose_name="نام")
    level = models.CharField(max_length=50,default="500 هزار تومان", verbose_name="شهریه")
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

