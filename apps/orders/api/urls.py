# Local
from django.urls import include, path
from rest_framework import routers

from apps.orders.api import views

app_name: str = "orders"

router = routers.SimpleRouter()
router.register(r"order", views.OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
