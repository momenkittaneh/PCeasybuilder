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


class product(models.Model):
    name= models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
    build_pc =models.ManyToManyField(users,through= 'cart')
    stock =models.IntegerField()
    categ = models.ForeignKey(catagory,related_name='prodtype',on_delete= CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class status(models.Model):
    status= models.CharField(max_length=15)
      

class order(models.Model):
    order_date= models.DateField(auto_now_add=True)
    order_price= models.IntegerField()
    status=models.ForeignKey(status,related_name="stat",on_delete=CASCADE)

class cart(models.Model):
    users_id=models.ForeignKey(users,on_delete=CASCADE)
    product_id=models.ForeignKey(product,on_delete=CASCADE)
    order_id = models.ForeignKey(order,related_name="cart",on_delete=CASCADE)
    total_price=models.IntegerField()
    quantity=models.IntegerField()


class troublshooting(models.Model):
    name=models.CharField(max_length=200) #name of problem
    desc = models.TextField()
    phone = models.CharField(max_length=200)
    order_id=models.ForeignKey(order,related_name="troubleshoot",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)






