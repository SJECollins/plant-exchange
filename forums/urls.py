from django.urls import path
from . import views


app_name = 'forums'
urlpatterns = [
    path('', views.ForumList.as_view(), name='forum_list'),
    path('forum/<forum_id>', views.ForumView.as_view(), name='forum'),
    path('new_topic/<forum_id>', views.TopicCreate.as_view(), name='new_topic'),
    # path('view_topic/<topic_id>', views.TopicView.as_view(), name='view_topic'),
    # path('edit_topic/<topic_id>', views.TopicEdit.as_view(), name='edit_topic'),
    # path('delete_topic/<topic_id>', views.TopicDelete.as_view(), name='delete_topic'),
    # path('<topic_id>/reply', views.Reply.as_view(), name='reply'),
    # path('edit_reply/<reply_id>', views.ReplyEdit.as_view(), name='edit_reply'),
    # path('delete_reply/<reply_id>', views.ReplyDelete.as_view(), name='delete_reply')
]