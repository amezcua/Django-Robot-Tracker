Django Robot Tracker
--------------------

Simple (naive) way to track robots.txt access.

Built for tracking access to robots.txt and recording the user-agent string of the clients accessing the file.

It allows you to take later actions on the requests based on a flag that tells if the request is being made by a well behaving robot.

Workflow.
---------

- A client accesses robots.txt on your site
- The user agent is recorded
- A flag is set in Django's request object
- Following requests with the same user agent string are flagged as a robot
- Other applications can check the flag to take appropiate action

Usage.
------

1. Add robot_tracker to your installed apps in the Django settings and sync the models with your db (syncdb, south, ...)

e.g.

INSTALLED_APPS = (
 ...
    'robot_tracker',
 ...
)

2. Add the middleware to your settings

e.g.

MIDDLEWARE_CLASSES = (
 ...
    'robot_tracker.middleware.TrackRobotsMiddleware',
 ...
)

3. Check for the is_robot flag in your request object

e.g.

if ('is_robot' in dir(request)) and request.is_robot:
    # Handle robot request
else:
    # Handle non robot request


Admin.
------
An admin page is provided so that you can easily see what user-agents have been recorded or to delete unwanted user-agents that might have been captured.


Lacking.
--------

The application right now does not do any caching so all requests hit the database to see if the user-agent is present in the robots table. Beware if you have a high traffic site.

Caveats.
--------

If you are serving the robots.txt file as a static file directly with Apache the Django app will not be hit and no recording of the user-agent will take place.