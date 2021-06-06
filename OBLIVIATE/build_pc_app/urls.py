from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('makeorder',views.makeorder),
    path('confirmorder',views.confirm),
    path('confirm',views.ok),
    path('cart',views.mycart),
    path('details/<int:id>',views.proddetails),
    path('orderdetails/<int:id>',views.proddetails),
    path('order', views.order_view),
    path('addquantity/<int:id>', views.addquantity),
    path('details/<int:id>', views.show_details),
    path('addtocart/<int:id>',views.addtocart),
    # path('troubeshoot',views.problem),
    
]
