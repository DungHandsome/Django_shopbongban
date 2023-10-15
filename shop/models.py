from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(null=True)
    slug = models.SlugField(max_length=1000)
    def __str__(self):
        return self.name
    

class product(models.Model):
    categery = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000)
    detail = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name