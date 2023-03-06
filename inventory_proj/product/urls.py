from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name="product"),
    path('add-product',views.add_product,name="add-product")
]