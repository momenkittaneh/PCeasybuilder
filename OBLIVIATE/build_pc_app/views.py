from django.http import request
from django.shortcuts import redirect, render
from .models import *

def home(request):
    if 'user_id' in request.session:
        context= {
            'log' : True,
            'getprof': get_user(request.session['user_id']),
            'product':get_products()
        }
        return render(request,"home.html",context)
    context={'product':get_products()}
    return render(request,"home.html",context)

def viewcart(request):
    context={
    'cartuser':get_user(request.session['user_id'])
    }
    return render(request,'cart.html',context)


def makeorder(request):

    return redirect('/confirmorder')

def confirm(request):
    context ={
        'log' : True,
        'user' : get_user(request.session['user_id']),
        'thecart': get_order()
    }
    return render(request,'makeorder.html',context)

def ok(request):
    theorder=create_order(request.session['user_id'])
    return redirect('/')

def mycart(request):
    mycart = view_cart(request.session['user_id'])
    context = {
        'log': True,
        'myitems': mycart
    }
    return render(request,'cart.html',context)
def proddetails(request,id):
    context ={
        'log':True,
        'det' : get_product(id)
    }
    return render(request,'details.html',context)

def myprofile(request):
    context ={
        'log':True,
        'user' : get_user(request.session['user_id'])
    }
    return render(request,'profile.html',context)

def addaddress(request,id):
    add = addnewaddress(id,request.post['state'],request.post['city'],request.post['street'])
    return redirect('/profile')
def order_view(request):
    context={
        'orders':get_order(request.session['user_id'])
    }
    return render(request,'order.html',context)

def addquantity(request,id):
    cart = update_quantity(id,request.POST['quantity'])
    return redirect('/cart')

def show_details(request,id):
    context = {
        'orddetail' : get_order_details(id)
    }