from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class v(admin.ModelAdmin):
    list_display = ['id','name','address','number']