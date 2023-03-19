import hashlib
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
    name = models.CharField(max_length=256, blank=False, null=False, help_text='Client name', verbose_name=u'Name')
    
    def __int__(self):
        return self.id
    
    
    def get_class_name(self):
        return "client"
    
    
class Buy(models.Model):
    cliente_id = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, help_text='Cliente_id', verbose_name=u'Cliente_id')
    
    total_to_pay = models.DecimalField(decimal_places=2, max_digits=10000, blank=False, null=False, help_text='Buy total_to_pay', verbose_name=u'Total_to_pay')
    
    card_number = models.CharField(max_length=256, blank=False, null=False, help_text='Buy card_number', verbose_name=u'Card_number')
    value = models.DecimalField(decimal_places=2, max_digits=10000, blank=False, null=False, help_text='Buy value', verbose_name=u'Value')
    cvv = models.CharField(max_length=3, blank=False, null=False, help_text='Buy cvv', verbose_name=u'Cvv')
    card_holder_name = models.CharField(max_length=256, blank=False, null=False, help_text='Buy card_holder_name', verbose_name=u'Card_holder_name')
    exp_date = models.CharField(max_length=4, blank=False, null=False, help_text='Buy exp_date', verbose_name=u'Exp_date')
    
    def save(self, *args, **kwargs):
        cipher_suite = Fernet('pakspokapoekae'.encode())
        encrypted_card_number = cipher_suite.encrypt(self.card_number[:12].encode()).decode()
        self.card_number = encrypted_card_number + self.card_number[12:]
        super(Buy, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.client_id} - {self.cliente_name} - ({self.encrypted_card_number}****)"
    
   
    

class History(models.Model):
    cliente_id = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, help_text='Cliente_id', verbose_name=u'Cliente_id')
    
    #purchase_id = models.ForeignKey(Buy, on_delete=models.CASCADE, blank=False, null=False, help_text='History purchase_id', verbose_name=u'Purchase_id')
    
    value = models.DecimalField(decimal_places=2, max_digits=10000, blank=False, null=False, help_text='History value', verbose_name=u'Value')
    date = models.DateField(blank=False, null=False, help_text='History date', verbose_name=u'Date')
    
    
    
    def __int__(self):
        return f"{self.client_id}  - ({self.encrypted_card_number}****) - "
            
                