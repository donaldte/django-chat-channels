from django.contrib import admin

from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','id')

admin.site.register(Message)    