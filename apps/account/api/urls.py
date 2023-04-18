# Local
from django.urls import include, path
from rest_framework import routers, urls

from apps.account.api import views

app_name = "account"

router = routers.SimpleRouter()
router.register(r"account", views.AccountViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
