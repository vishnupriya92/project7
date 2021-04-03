from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to index of app2</h1>")

def sample2(request):
    return render(request,"app2/sample2.html")
    