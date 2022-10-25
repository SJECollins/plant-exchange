from django.urls import path
from . import views


app_name = 'profiles'
urlpatterns = [
    path('<user_id>', views.ProfileView.as_view(), name='profile'),
    path('create_profile/', views.ProfileCreate.as_view(), name='create_profile'),
    path('edit/<pk>', views.ProfileUpdate.as_view(), name='edit_profile')
]