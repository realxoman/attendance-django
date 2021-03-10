from django.contrib import admin
from .models import TarahiClass,UserTerm,Jalase
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin

admin.site.site_title = "چهره پردازان"
admin.site.index_title = "مدیریت حضور و غیاب"
admin.site.site_header = "مدیریت حضور و غیاب چهره پردازان"

# Register your models here.
class Jalase_Inline(StackedInlineJalaliMixin,admin.StackedInline):
    model = Jalase
    extra = 1


class UserTermAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('classname','user')
    inlines = (
        Jalase_Inline,
    )
    

admin.site.register(TarahiClass)
admin.site.register(UserTerm,UserTermAdmin)
admin.site.register(Jalase)