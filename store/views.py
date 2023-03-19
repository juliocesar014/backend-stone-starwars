from rest_framework import viewsets, generics
from store.models import Product, Client, Buy, History
from store.serializer import ProductSerializer, ClientSerializer, BuySerializer, HistorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    
class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    
    
class ClientHistoryView(generics.ListAPIView):
    #Listar compras de um cliente
    def get_queryset(self):
        queryset = History.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = HistorySerializer