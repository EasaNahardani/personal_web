from django.contrib import admin
from .models import Skill, ContactMessage

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'level')
    list_filter = ('name', 'level')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sender_mail', 'sender_phone', 'sent_at')
    list_filter = ('sent_at', )
    search_fields = ('full_name', 'sender_mail', 'sender_phone')
