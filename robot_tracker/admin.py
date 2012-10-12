from django.contrib import admin
from models import RobotUserAgent

class RobotUserAgentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    ordering = ('user_agent',)
    list_display = ('user_agent', 'created',)
    

admin.site.register(RobotUserAgent, RobotUserAgentAdmin)