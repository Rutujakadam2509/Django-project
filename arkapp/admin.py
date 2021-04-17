from django.contrib import admin
from .models import student,studentdetails
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_display=['rollno','name']
  list_display=['rollno','name']

admin.site.register(student,StudentAdmin)

class StudentdetailsAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','sub','marks','grade']

admin.site.register(studentdetails, StudentdetailsAdmin)
