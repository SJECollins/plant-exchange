from django.urls import path
from . import views


app_name = 'plantblog'
urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post_detail/<post_id>', views.PostDetail.as_view(), name='post'),
    path('like/<post_id>', views.PostLike.as_view(), name='post_like')
]