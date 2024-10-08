from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def explore(request):
    return render(request,'explore.html')

def about(request):
    return render(request,'about.html')

def generator(request):
    return render(request,'generator.html')


def documentation(request):
    return render(request,'doumentation.html')