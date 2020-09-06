from django.contrib import admin
from .models import Studentinfo,Studentmark
# Register your models here.

@admin.register(Studentinfo)
class adminstudent(admin.ModelAdmin):
    list_display = ['id','name','father_n']



@admin.register(Studentmark)
class adminstudent(admin.ModelAdmin):
    list_display = ['id','name' , 'maths']