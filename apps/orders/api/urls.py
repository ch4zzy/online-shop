from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

# Local
from . import views

app_name = 'orders'
router = routers.SimpleRouter()
router.register(r'order', views.OrderViewSet)

api_view = get_swagger_view(title="Api")

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-docs/', api_view),
]

