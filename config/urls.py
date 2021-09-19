from django.contrib import admin
from django.db.models.expressions import F
from django.urls import path, include
from rest_framework import routers
from client.views import ClientViewSet
from category.views import CategoryViewSet


router = routers.DefaultRouter()
router.register('client', ClientViewSet)
router.register('category', CategoryViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework page
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]
