# Local
from django.urls import path

from apps.coupons import views

app_name = "coupons"


urlpatterns = [
    path("apply/", views.coupon_apply, name="apply"),
]
