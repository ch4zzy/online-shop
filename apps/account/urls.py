# Local
from apps.account import views
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
