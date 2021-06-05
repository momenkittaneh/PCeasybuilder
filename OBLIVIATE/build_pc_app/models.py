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
    build_pc =models.ManyToManyField(users,through= 'cart')
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
    def __str__(self):
        return self.name






