from django.shortcuts import render,HttpResponse
from .models import studentdetails

# Create your views here.
# def index(request):
#     Student=student.objects.all()
#     return render(request,'result.html',{'Student':Student})

def student(request):
    STUDENT=studentdetails.objects.all()
    return render(request,'index.html',{'STUDENT':STUDENT})