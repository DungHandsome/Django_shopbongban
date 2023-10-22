from django.urls import path
from . import views
urlpatterns = [
    path('', views.shop, name="home"),
    path('product/', views.products, name='product'),
]