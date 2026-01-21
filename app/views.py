from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def addstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['mail']
        age=request.POST['age']
        phone=request.POST['phone']
        course=request.POST['course']
        data= Students.objects.create(name=name,email=email,age=age,phone=phone,course=course)
        data.save()
        print('student registered successfully')
        return redirect(index)
    return render(request,'addstudent.html')

def index(request):
    stds = Students.objects.all()
    return render(request,'index.html',{'stds':stds})


def update(request,pk):
    std = Students.objects.get(pk=pk)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['mail']
        age=request.POST['age']
        phone=request.POST['phone']
        course=request.POST['course']
        Students.objects.filter(pk=pk).update(name=name,email=email,age=age,phone=phone,course=course) 
        return redirect(index)
    return render(request,'update.html',{'std':std})

def delete(request,pk):
    Students.objects.get(pk=pk).delete()
    return redirect(index)