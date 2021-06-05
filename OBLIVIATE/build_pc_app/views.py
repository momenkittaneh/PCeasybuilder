from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index2(reqeust):
    return render(reqeust,"home.html")