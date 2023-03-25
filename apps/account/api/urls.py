from django.urls import path

# Local
from . import views
app_name = 'account'


urlpatterns = [
    path('profile/', views.ProfileAPIView.as_view()),
    path('profile/<int:pk>/', views.ProfileAPIView.as_view()),
]
