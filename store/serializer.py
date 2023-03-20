from rest_framework import serializers
from store.models import Product, Client, Buy


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price','zipcode','seller', 'thumbnailHd', 'date']
        
        
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']
        
        
class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = ['id', 'cliente_id', 'value', 'data', 'card_number', ]
    
    def get_card_number(self, obj):
        return '**** **** **** ' + obj.card_number[-4:]
        
        