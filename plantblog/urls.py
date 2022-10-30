from django.urls import path
from . import views


app_name = 'plantblog'
urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post_detail', views.PostDetail.as_view(), name='post')
]