from django.urls import path
from . import views


app_name = 'profiles'
urlpatterns = [
    path('<user_id>', views.ProfileView.as_view(), name='profile'),
    path('edit/<pk>', views.ProfileUpdate.as_view(), name='edit_profile'),
    path('new_message/<plant_id>', views.MessageCreate.as_view(), name='new_message'),
    path('mailbox/', views.MailboxList.as_view(), name='mailbox'),
    path('message/<msg_id>', views.MessageView.as_view(), name='message'),
]