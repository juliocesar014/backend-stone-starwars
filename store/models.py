import hashlib
import uuid
from django.db import models
from cryptography.fernet import Fernet

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False, help_text='Product title', verbose_name=u'Title')
    price = models.DecimalField(decimal_places=2, max_digits=10000, blank=False, null=False, help_text='Product price', verbose_name=u'Price')
    zipcode = models.CharField(max_length=256, blank=False, null=False, help_text='Product zipcode', verbose_name=u'Zipcode')
    seller = models.CharField(max_length=256, blank=False, null=False, help_text='Product seller', verbose_name=u'Seller')
    thumbnailHd = models.CharField(max_length=256, blank=False, null=False, help_text='Product thumbnailHd', verbose_name=u'ThumbnailHd')
    date = models.DateField(blank=False, null=False, help_text='Product date', verbose_name=u'Date')


    def __int__(self):
        return self.id

    def __str__(self):
        return self.title
    


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, blank=False, null=False, help_text='Client name', verbose_name=u'Name')
    
    def __int__(self):
        return self.id
    
    
    def get_class_name(self):
        return "client"
    
    
class Buy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    cliente_id = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, help_text='Cliente', verbose_name=u'Cliente')
    
    produto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, help_text='Produto', verbose_name=u'Produto')
    
    
    
    card_number = models.CharField(max_length=16, blank=False, null=False, help_text='Card_number', verbose_name=u'Card_number')
    cvv = models.CharField(max_length=3, blank=False, null=False, help_text='Buy cvv', verbose_name=u'Cvv')
    card_holder_name = models.CharField(max_length=256, blank=False, null=False, help_text='Buy card_holder_name', verbose_name=u'Card_holder_name')
    exp_date = models.CharField(max_length=5, blank=False, null=False, help_text='Buy exp_date', verbose_name=u'Exp_date')
    
    value = models.DecimalField(decimal_places=2, max_digits=10000, blank=False, null=False, help_text='History value', verbose_name=u'Value')
    data = models.DateField(blank=False, null=True, help_text='History data', verbose_name=u'Data')
    
   
    
    def __int__(self):
        return self.id
    
   
    
          