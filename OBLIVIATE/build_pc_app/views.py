from django.shortcuts import redirect, render
from .models import *

def home(request):
    if 'id' in request.session:
        context= {
            'log' : True,
            'getprof': get_user(request.session['id'])
        }
        return render(request,"home.html",context)
    return render(request,"home.html")

def viewcart(request):
    context={
    'cartuser':get_user(request.session['user_id'])
    }
    return render(request,'cart.html',context)


def makeorder(request):
    return redirect('/confirmorder')

def confirm(request):
    context ={
        'user' : get_user(request.session['user_id']),
        'thecart': get_order()
    }
    return render(request,'makeorder.html',context)

def ok(request):
    theorder=create_order(request.session['user_id'])
    return redirect('/')