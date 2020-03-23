from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bride(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True)
    brand = models.CharField(max_length=30, default="anonymous")
    size = models.CharField(max_length=30, default="anonymous")
    price = models.IntegerField(null=True)
    describe = models.TextField(default="About the product specs")

    def __str__(self):
        return self.name


class Cart(models.Model):
    user_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)

    def __str__(self):
        return self.user_id


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
