from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('enquetes', views.enquetes, name='enquetes'),
    path ('dashboard', views.dashboard, name= 'dashboard')
]