from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to index of app1</h1>")

def sample1(request):
    return render(request,"app1/sample1.html")
    