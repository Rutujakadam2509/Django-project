from django.db import models

# Create your models here.
class student(models.Model):
      rollno=models.IntegerField()
      name=models.CharField(max_length=255)

class studentdetails(models.Model):
      rollno=models.IntegerField()
      name=models.CharField(max_length=255)
      sub=models.CharField(max_length=255)
      marks=models.IntegerField()
      grade=models.CharField(max_length=10)



