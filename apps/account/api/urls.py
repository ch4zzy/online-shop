from django.urls import path, include
from rest_framework import routers, urls

# Local
from apps.account.api import views


app_name = 'account'

router = routers.SimpleRouter()
router.register(r'account', views.AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
