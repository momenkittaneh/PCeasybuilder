from django.http import request
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(reqeust):
    return render(request,'index.html')
