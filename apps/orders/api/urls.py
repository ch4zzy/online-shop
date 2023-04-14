from django.urls import path, include
from rest_framework import routers

# Local
from . import views


app_name = 'orders'

router = routers.SimpleRouter()
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

