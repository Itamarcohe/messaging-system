from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'created_at', 'is_read')
    list_filter = ('sender', 'receiver', 'is_read', 'created_at')
    ordering = ('-created_at',)


admin.site.register(Message, MessageAdmin)


