from django.shortcuts import redirect, render
from .models import *

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

# def ok(request):
#     theorder=create_order(order_price=)
    