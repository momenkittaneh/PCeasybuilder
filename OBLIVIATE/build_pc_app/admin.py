from django.contrib import admin

# Register your models here.
from .models import *
class postimageAdmin(admin.StackedInline):
    model=postimage

admin.site.register(catagory)
admin.site.register(brand)

admin.site.register(status)
admin.site.register(order)
admin.site.register(troublshooting)


@admin.register(product)
class postadmin(admin.ModelAdmin):
    inlines=[postimageAdmin]
    class meta:
        model = product
        
@admin.register(postimage)
class postimageAdmin(admin.ModelAdmin):
    pass