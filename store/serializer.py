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
        fields = ['id', 'cliente_id', 'value', 'data', 'card_number']

    def format_card_number(self, card_number):
        # Insere asteriscos e retorna a string formatada
        return '**** **** **** ' + card_number[-4:]

    def to_representation(self, instance):
        # Chama a função format_card_number para formatar o card_number
        ret = super().to_representation(instance)
        ret['card_number'] = self.format_card_number(ret['card_number'])
        return ret

    

        
        