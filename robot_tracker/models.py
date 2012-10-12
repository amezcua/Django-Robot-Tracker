# -*- coding: utf-8 -*-
from django.db import models

class RobotUserAgent(models.Model):
    created = models.DateField(auto_now_add=True)
    user_agent = models.CharField(max_length=1024, unique=True)

    def __unicode__(self):
        return self.user_agent
    
    def create_ua(self, ua_string):
        try:
            rua = RobotUserAgent()
            rua.user_agent = ua_string
            # Todo. Add to memory cache
            rua.save()
        except:
            pass
        
    def get_ua(self, ua_string):
        # Todo. Check in memory cache
        try:
            return RobotUserAgent.objects.get(user_agent=ua_string)
        except:
            return None