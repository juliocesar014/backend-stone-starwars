from rest_framework import viewsets, generics
from store.models import Product, Client, Buy
from store.serializer import ProductSerializer, ClientSerializer, BuySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    
class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer


class BuyHistoryAPIView(generics.ListAPIView):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer