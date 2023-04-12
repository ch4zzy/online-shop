"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# Local
from config.yasg import urlpatterns as api_docs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('account/', include('apps.account.urls')),
    path('payment/', include('apps.payment.urls', namespace='payment')),
    path('coupons/', include('apps.coupons.urls', namespace='coupons')),
    path('', include('apps.shop.urls', namespace='shop')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('api/shop/', include('apps.shop.api.urls', namespace='api')),
    path('api/account/', include('apps.account.api.urls', namespace='api_cat')),
    path('api/orders/', include('apps.orders.api.urls', namespace='api_order')),
    path('api/drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += api_docs

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
