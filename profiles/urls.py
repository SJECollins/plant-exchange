from django.urls import path
from . import views

urlpatterns = [
    path('<user_id>', views.ProfileView.as_view(), name='profile'),
]