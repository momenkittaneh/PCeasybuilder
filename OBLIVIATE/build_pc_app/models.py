from django.db import models
from django.db.models.deletion import CASCADE
from login_reg_app.models import *


class address(models.Model):
    state=models.CharField(max_length=200) #name of problem
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    user_id=models.ForeignKey(users,related_name="address",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class catagory(models.Model):
    name= models.CharField(max_length=20)
    def __str__(self):
        return self.name
class brand(models.Model):
    name= models.CharField(max_length=20)
    catbrand= models.ForeignKey(catagory,related_name="brands",on_delete=CASCADE)
    def __str__(self):
        return self.name

class product(models.Model):
    name= models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
    build_pc =models.ManyToManyField(users,through= 'cart',related_name="products")
    orders= models.ManyToManyField('order',through='cart',related_name='products')
    stock =models.IntegerField()
    categ = models.ForeignKey(brand,related_name='prodtype',on_delete= CASCADE)
    thumb = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class postimage(models.Model):
    post=models.ForeignKey(product,default=None,on_delete=CASCADE)
    thumb=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.post.name

class status(models.Model):
    status= models.CharField(max_length=15)
    def __str__(self):
        return self.status
     

class order(models.Model):
    order_date= models.DateField(auto_now_add=True)
    order_price= models.IntegerField()
    status=models.ForeignKey(status,related_name="stat",on_delete=CASCADE)
    productorder =models.ManyToManyField(product,through= 'cart')
    user_order= models.ForeignKey(users,related_name="orders",on_delete=CASCADE,default=None)




class cart(models.Model):
    users_id=models.ForeignKey(users,related_name="mycart",on_delete=CASCADE)
    product_id=models.ForeignKey(product,on_delete=CASCADE)
    order_id = models.ForeignKey(order,related_name="cart",on_delete=CASCADE ,default=None)
    total_price=models.IntegerField()
    quantity=models.IntegerField()



class troublshooting(models.Model):
    name=models.CharField(max_length=200) #name of problem
    desc = models.TextField()
    phone = models.CharField(max_length=200)
    order_id=models.ForeignKey(order,related_name="troubleshoot",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


def get_products():
    return product.objects.all()

def get_order(user_id):
    user=users.objects.get(id=user_id)
    ord=order.objects.filter(user_order=user)
    return ord


def create_order(id):
    user= users.objects.get(id=id)
    det=user.mycart.all()
    ord = order.objects.create(order_price=det.total_price,user_order=user)
    return ord


def view_cart(id):
    user= users.objects.get(id=id)
    return user.mycart.all()


def get_product(id):
    prod = product.objects.get(id=id)
    return prod

def addnewaddress(id,state,city,street):
    user = users.objects.get(id=id)
    adres = address.objects.create(state=state,city=city,street=street,user_id=user)
    return adres

def update_quantity(id,quantity):
    newcart= cart.objects.get(id=id)
    newcart.quantity= quantity
    newcart.save()
    return newcart

def get_order_details(id):
    return order.object.get(id=id)
