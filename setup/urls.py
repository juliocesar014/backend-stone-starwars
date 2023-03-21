from django import views
from django.contrib import admin
from django.urls import include, path
from store.views import ProductViewSet, ClientViewSet, BuyViewSet, BuyHistoryAPIView
from rest_framework import routers
from rest_framework import permissions
from store import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="API STARS WARS STORE (STONE CHALLENGE))",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juliocesar014@live.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='Products')
router.register('clients', ClientViewSet, basename='Clients')
router.register('buys', BuyViewSet, basename='Buys')
#router.register('history', HistoryViewSet, basename='History')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('history/<int:client_id>/', ClientHistoryView.as_view(), name='client_history'),
    path('starstore/', include(router.urls)),
    path('starstore/history/', views.BuyHistoryAPIView.as_view(), name='history'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   
]
