from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name ='index'),
    path('base/', views.base, name ='base'),
    path('shop/', views.shop, name ='shop'),
]