from django.shortcuts import render
from .models import *
# Create your views here.
def shop(request):
    Infocategory = Category.objects.all().order_by('name')
    Infoproduct = product.objects.all().order_by('date')
    context = {
        "Infocategory": Infocategory,
        "Infoproduct": Infoproduct,
    }
    return render(request, 'shop/shop.html', context)

def products(request):
    id = request.GET.get('id')
    Infoproduct = product.objects.filter(id=id)
    return render(request, 'shop/product.html', {"Infoproduct" : Infoproduct})