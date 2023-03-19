from rest_framework import serializers
from store.models import Product, Client, Buy, History


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'thumbnailHd', 'date']
        
        
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']
        
        
class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = ['id', 'cliente_id', 'total_to_pay', 'card_number', 'value', 'cvv', 'card_holder_name', 'exp_date']
        
        
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'cliente_id', 'purchase_id', 'value', 'date']