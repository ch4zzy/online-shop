from django.urls import path

# Local
from . import views

app_name = 'shop'


urlpatterns = [
    path('category/', views.CategoryAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryAPIView.as_view()),
    path('product/', views.ProductAPIView.as_view()),
    path('product/<int:pk>', views.ProductAPIView.as_view()),
]
