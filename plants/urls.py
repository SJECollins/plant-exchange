from django.urls import path
from . import views


app_name = 'plants'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('exchange/', views.PlantList.as_view(), name='exchange'),
    path('<int:plant_id>/', views.PlantDetail.as_view(), name='plant_detail'),
    path('add/', views.AddPlant.as_view(), name='add_plant'),
]