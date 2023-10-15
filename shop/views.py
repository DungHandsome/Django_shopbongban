from django.shortcuts import render
from .models import Category, product
# Create your views here.
def shop(request):
    Infocategory = {'Infocategory': Category.objects.all().order_by('name')}
    return render(request, 'shop/shop.html', Infocategory)