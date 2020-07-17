from django.contrib import admin

# Register your models here.
from api.models import *


class UserModeEvent(admin.ModelAdmin):
   list_display = ('id', 'name','last_login', 'email', 'password')


class EventModeEvent(admin.ModelAdmin):
   list_display = ('id', 'title', 'level', 'address', 'date_event', 'detail', 'arquivado', 'user_id')


admin.site.register(User, UserModeEvent)
admin.site.register(Event, EventModeEvent)
