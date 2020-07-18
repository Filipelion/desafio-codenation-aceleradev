'''from django.contrib import admin

# Register your models here.
from api.models import *


class UserModeEvent(admin.ModelAdmin):
   list_display = ('id', 'name','last_login', 'email', 'password')


class EventModeEvent(admin.ModelAdmin):
   list_display = ('id', 'title', 'level', 'address', 'date_event', 'detail', 'arquivado', 'user_id')


admin.site.register(User, UserModeEvent)
admin.site.register(Event, EventModeEvent)
'''

from __future__ import unicode_literals
import logging

from django.contrib import admin
from django.utils.html import format_html

from api.models import *


class UserModeEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_login', 'email', 'password')


class StatusLogAdmin(admin.ModelAdmin):
    list_display = ('level','colored_msg', 'address', 'traceback', 'arquivado', 'date_event')
    list_display_links = ('colored_msg',)
    list_filter = ('level',)
    list_per_page = 10

    def colored_msg(self, instance):
        if instance.level in [logging.NOTSET, logging.INFO]:
            color = 'green'
        elif instance.level in [logging.WARNING, logging.DEBUG]:
            color = 'orange'
        else:
            color = 'red'

        return format_html('<span style="color: {color};">{detail}</span>', color=color, detail=instance.detail)
    colored_msg.short_description = 'Mensagem'

    def traceback(self, instance):
        return format_html('<pre><code>{content}</code></pre>', content=instance.trace if instance.trace else '')

    traceback.short_description = 'Detalhes'

    def create_datetime_format(self, instance):
        return instance.date_event.strftime('%d-%m-%Y %X')

    create_datetime_format.short_description = 'Data do log'


admin.site.register(User, UserModeEvent)
admin.site.register(Event, StatusLogAdmin)
