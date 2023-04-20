# Local
from django.urls import include, path
from rest_framework import routers

from apps.shop.api import views

app_name: str = "shop"


router = routers.SimpleRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"product", views.ProductViewSet)
router.register(r"comment", views.CommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
