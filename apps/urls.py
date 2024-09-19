from django.urls import path
from . import views 
from .views import BrandDetailView, CarBrandListView, CarDetailView, CarsView 

urlpatterns = [
   path('brands/', CarBrandListView.as_view(), name = 'brands'),
   path('cars/', CarsView.as_view(), name = 'cars'),
   path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
   path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]