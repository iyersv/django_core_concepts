from django.urls import path,include
from products.views import home

urlpatterns = [
    path('',home),
]