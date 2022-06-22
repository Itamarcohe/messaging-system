from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'subject', 'is_read')
    list_filter = ('sender', 'receiver', 'created_at', 'is_read')


admin.site.register(Message, MessageAdmin)

