from django.contrib import admin
from . models import *
# Register your models here.

class categadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(categ,categadmin)

class productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','price','stock']
    list_editable = ['price','stock']
admin.site.register(products,productadmin)