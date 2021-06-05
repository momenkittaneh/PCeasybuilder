from django.http import request
from django.shortcuts import render,HttpResponse,redirect
import bcrypt
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,"index.html")

def register(request):
    errors = users.objects.register(request.POST)
    if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    first_name= request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
    if password == confirm_password:
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = create_user(first_name,last_name,email,pw_hash)
    if user:
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
    return redirect('/')
def login(request):
    user = login_user(request.post['email'])
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['first_name'] = logged_user.first_name
            request.session['last_name'] = logged_user.last_name

            return redirect('/')
    return redirect("/log")

def logout(request):
    request.session.clear()
    return redirect('/')