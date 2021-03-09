from django.contrib import admin
from .models import TarahiClass,UserTerm,Jalase

# Register your models here.
class Jalase_Inline(admin.TabularInline):
    model = Jalase
    extra = 8


class UserTermAdmin(admin.ModelAdmin):
    list_display = ('classname','user')
    inlines = [
        Jalase_Inline,
    ]

admin.site.register(TarahiClass)

admin.site.register(UserTerm,UserTermAdmin)

admin.site.register(Jalase)