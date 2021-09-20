from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from client.views import ClientViewSet
from category.views import CategoryViewSet
from cart.views import CartViewSet
from product.views import ProductViewSet


router = routers.DefaultRouter()
router.register('client', ClientViewSet)
router.register('category', CategoryViewSet)
router.register('cart', CartViewSet)
router.register('product', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework page
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]
