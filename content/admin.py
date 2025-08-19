from django.contrib import admin
from .models import Chat, Message, Story


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass