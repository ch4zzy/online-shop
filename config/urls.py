from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Local

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("apps.orders.urls", namespace="orders")),
    path("cart/", include("apps.cart.urls", namespace="cart")),
    path("account/", include("apps.account.urls")),
    path("payment/", include("apps.payment.urls", namespace="payment")),
    path("coupons/", include("apps.coupons.urls", namespace="coupons")),
    path("", include("apps.shop.urls", namespace="shop")),
    path("social-auth/", include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
