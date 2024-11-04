from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index-url'),
    path('contact/',views.contact,name='contact-url'),
]


