from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import MessageCreateView, ChatListView, MessageListView,StoryListView, StoryCreateView

urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('<int:chat_id>/messages/', MessageListView.as_view(), name='message_list'),
    path('<int:chat_id>/messages/send/', MessageCreateView.as_view(), name='message_create'),
    path("chats/<int:chat_id>/stories/", StoryListView.as_view(), name="story-list"),
    path("<int:chat_id>/stories/create/",StoryCreateView.as_view(), name="story-create"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
