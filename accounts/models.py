from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

#main user
class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    def __str__(self):
        return self.username


#seller
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='seller')
    def __str__(self):
        return self.user.username    


#buyer
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='buyer')
    def __str__(self):
        return self.user.username


#product or item model 
class ItemModel(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.CharField(max_length=500)
    picture = models.URLField()
    item_name = models.CharField(max_length=500) 
    item_description = models.CharField(max_length=1000)
    post_on = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return self.item_name

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='card')
    item = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    cart_on = models.DateTimeField(auto_now_add=timezone.now())
    def __str__(self):
        return self.item.item_name and self.user.username


class Buy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='buy')
    item = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    buy_on = models.DateTimeField(auto_now_add=timezone.now())
    def __str__(self):
        return self.item.item_name and self.user.username



