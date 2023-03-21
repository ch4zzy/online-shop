from django.urls import path

# Local
from . import views

app_name = 'shop'


urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/', views.CategoryDetailView.as_view(), name='category_detail'),
]

