from django.shortcuts import render
from .models import Category, product
# Create your views here.
def shop(request):
    Infocategory = Category.objects.all().order_by('name')
    Infoproduct = product.objects.all().order_by('date')
    context = {
        "Infocategory": Infocategory,
        "Infoproduct": Infoproduct,
    }
    return render(request, 'shop/shop.html', context)

def products(request, id):
    Infoproduct = product.objects.get(id=id)
    return render(request, 'shop/product.html', {"Infoproduct" : Infoproduct})

def categories(request, slug):
    Infocategory = Category.objects.get(slug=slug)
    Infoproduct = product.objects.filter(categery__slug=slug)
    return render(request, 'shop/category.html', {"Infocategory" : Infocategory, "Infoproduct" : Infoproduct})