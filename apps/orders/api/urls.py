# Local
from apps.orders.api import views
from django.urls import include, path
from rest_framework import routers

app_name = 'orders'

router = routers.SimpleRouter()
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
