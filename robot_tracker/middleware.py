# -*- coding: utf-8 -*-

from models import RobotUserAgent

class TrackRobotsMiddleware(object):
      
    def process_request(self, request):
        try:
            ua_string = request.META['HTTP_USER_AGENT']
            if request.path == '/robots.txt':
                request.is_robot = True
                if not RobotUserAgent().get_ua(ua_string):
                    RobotUserAgent().create_ua(ua_string)
            else:
                request.is_robot = False
                try:
                    if RobotUserAgent().get_ua(ua_string):
                        request.is_robot = True
                except:
                    pass
        except:
            pass

        