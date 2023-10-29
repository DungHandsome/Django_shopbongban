from django.urls import path
from . import views
urlpatterns = [
    path('', views.shop, name="home"),
    path('<int:id>/', views.products, name='product'),
    path('<slug:slug>/', views.categories, name='category'),
]