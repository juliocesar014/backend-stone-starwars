from django import views
from django.contrib import admin
from django.urls import include, path
from store.views import ProductViewSet, ClientViewSet, BuyViewSet, BuyHistoryAPIView
from rest_framework import routers
from rest_framework import permissions
from store import views

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='Products')
router.register('clients', ClientViewSet, basename='Clients')
router.register('buys', BuyViewSet, basename='Buys')
#router.register('history', HistoryViewSet, basename='History')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('history/<int:client_id>/', ClientHistoryView.as_view(), name='client_history'),
    path('', include(router.urls)),
    path('history/', views.BuyHistoryAPIView.as_view(), name='history'),
   
]
