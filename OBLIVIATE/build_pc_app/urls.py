from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('makeorder',views.makeorder),
    path('confirmorder',views.confirm),
    path('confirm',views.ok),
    path('cart',views.mycart),
    path('details/<int:id>',views.proddetails),
<<<<<<< HEAD
    path('profile',views.myprofile),
    path('addaddress/<int:id>',views.addaddress),
=======
    path('order/<int:id>', views.order_view),
>>>>>>> b8396824de2f47a231faf9eb2ca7735bbc0c3cf4
    
]
