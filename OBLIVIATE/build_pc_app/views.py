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
def homefilter(request,filter):
    ob=filter_products(filter)    
    if 'user_id' in request.session:
        context= {
            'log' : True,
            'getprof': get_user(request.session['user_id']),
            'product': ob}
        return render(request,"home.html",context)
    context={'product':ob}
    return render(request,"home.html",context)


def viewcart(request):
    if 'user_id' in request.session:

        context={
        'cartuser':get_user(request.session['user_id'])
        }
        return render(request,'cart.html',context)
    return redirect('/log')


def makeorder(request):

    return redirect('/confirmorder')

def confirm(request):
    context ={
        'log' : True,
        'user' : get_user(request.session['user_id']),
        'thecart': get_cart(request.session['user_id'])
    }
    return render(request,'makeorder.html',context)

def ok(request):
    theorder=create_order(request.session['user_id'])
    return redirect('/')

def mycart(request):
    if 'user_id' in request.session:
        mycart = view_cart(request.session['user_id'])
        context = {
            'log': True,
            'myitems': mycart
        }
        return render(request,'cart.html',context)
    return redirect('/log')

def proddetails(request,id):
    context ={
        'log':True,
        'det' : get_product(id)
    }
    return render(request,'details.html',context)

def myprofile(request):
    if 'user_id' in request.session:

        context ={
            'log':True,
            'user' : get_user(request.session['user_id'])
        }
        return render(request,'profile.html',context)
    return redirect('/log')

def addaddress(request,id):
    add = addnewaddress(id,request.post['state'],request.post['city'],request.post['street'])
    return redirect('/profile')
def order_view(request):
    if 'user_id' in request.session:

        context={
            'orders':get_order(request.session['user_id'])
        }
        return render(request,'order.html',context)
    return redirect('/log')

def addquantity(request,id):
    cart = update_quantity(id,request.POST['quantity'])
    return redirect('/cart')

def show_details(request,id):
    context = {
        'orddetail' : get_order_details(id)
    }

def  addtocart(request,id):
    if 'user_id' in request.session:

        user = get_user(request.session['user_id'])
        getprod = product.objects.get(id=id)
        carting = cart.objects.create(users_id=user,product_id=getprod,quantity=1)
        return redirect('/cart')
    return redirect('/log')

def problem(request):
    return render(request,"troubleshoot.html")