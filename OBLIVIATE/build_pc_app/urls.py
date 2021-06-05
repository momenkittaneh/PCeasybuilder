from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('makeorder',views.makeorder),
    path('confirmorder',views.confirm),
    path('confirm',views.ok)
]
