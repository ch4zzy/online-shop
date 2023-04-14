from django.urls import path, include
from rest_framework import routers

# Local
from apps.shop.api import views


app_name = 'shop'


router = routers.SimpleRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
