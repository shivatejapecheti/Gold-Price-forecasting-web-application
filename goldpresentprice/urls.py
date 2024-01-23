
from django.urls import path
from . import views

urlpatterns = [
    path('goldpresentprice/',views.goldpresentprice,name='goldpresentprice')

]
