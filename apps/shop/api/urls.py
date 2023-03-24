from django.urls import path

# Local
from . import views

app_name = 'shop'


urlpatterns = [
    path('category/', views.CategoryAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryAPIView.as_view()),

    path('product/', views.ProductAPIView.as_view()),
    path('product/<int:pk>', views.ProductAPIView.as_view()),

    
    #path('category/', views.CategoryListView.as_view(), name='category_list'),
    #path('category/', views.CategoryDetailView.as_view(), name='category_detail'),
    #path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    #path('category/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    #path('product/', views.ProductListView.as_view(), name='product_list'),
    #path('product/', views.ProductDetailView.as_view(), name='product_detail'),
]

