from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def add(request):
    try:
        a=int(request.GET['t1'])
        b=int(request.GET['t2'])
        c=a+b
        return HttpResponse("<html><body bgcolor=cyan><h1>Sum is:"+str(c)+"</h1></body></html>")
    except(ValueError):
        return HttpResponse("Invalid Input")

