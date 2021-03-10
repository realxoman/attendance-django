from django.contrib import admin
from .models import TarahiClass,UserTerm,Jalase


admin.site.site_title = "چهره پردازان"
admin.site.index_title = "مدیریت حضور و غیاب"
admin.site.site_header = "مدیریت حضور و غیاب چهره پردازان"

# Register your models here.
class Jalase_Inline(admin.TabularInline):
    model = Jalase
    extra = 0


class UserTermAdmin(admin.ModelAdmin):
    list_display = ('classname','user')
    inlines = [
        Jalase_Inline,
    ]

admin.site.register(TarahiClass)

admin.site.register(UserTerm,UserTermAdmin)

admin.site.register(Jalase)