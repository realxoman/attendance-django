from django.contrib import admin
from .models import TarahiClass,UserTerm,Jalase,Profile
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin

from django.contrib.auth.models import User

from .models import Profile

admin.site.site_title = "چهره پردازان"
admin.site.index_title = "مدیریت حضور و غیاب"
admin.site.site_header = "مدیریت حضور و غیاب چهره پردازان"

# Register your models here.
class Jalase_Inline(StackedInlineJalaliMixin,admin.StackedInline):
    model = Jalase
    extra = 1

class classnameAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'پروفایل'
    fk_name = 'user'
    
class UserProfileAdmin(admin.ModelAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','get_phonenumber')
    list_filter = ['is_superuser' , 'is_staff']
    search_fields = ['username','first_name','last_name','profile__phoneNumber']
    list_select_related = ('profile', )
    
    def get_phonenumber(self, instance):
        return instance.profile.phoneNumber
    get_phonenumber.short_description = 'تلفن همراه'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserProfileAdmin, self).get_inline_instances(request, obj)

class UserTermAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('classname','user','payment_status','class_status')
    list_filter = ['classname','payment_status','class_status','date_payment']
    inlines = (
        Jalase_Inline,
    )
    search_fields = ['user__username','user__first_name','user__last_name','classname__name']
    autocomplete_fields = ['user','classname']





admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(TarahiClass,classnameAdmin)
admin.site.register(UserTerm,UserTermAdmin)
admin.site.register(Jalase)