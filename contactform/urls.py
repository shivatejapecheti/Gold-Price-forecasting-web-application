from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('success/', views.success_view, name='success'),  # New URL for success page

]