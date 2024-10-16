from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField


# Create your models here.
class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("apps.Category", on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    size = CharField(max_length=50)
    color = CharField(max_length=50)

    def __str__(self):
        return self.name
