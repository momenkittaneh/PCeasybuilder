from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(catagory)
admin.site.register(brand)
admin.site.register(product)
admin.site.register(status)
admin.site.register(order)
admin.site.register(troublshooting)

