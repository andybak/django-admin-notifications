django-admin-notifications
==========================

A simple app to allow apps to register notifications that can be displayed in the admin via a template tag


Installation
------------

Add 'admin_notifications' to INSTALLED_APPS


Basic usage
-----------


Customize whichever of your admin templates you which to display the notifications thus.

load the template tags at the start of the template::

    {% load notification_tag %}

add the tag to your template. I customised the admin index template and placed the tag before the 'content-main' DIV like thus::

    {% block content %}
    <!-- here's the tag you add -->
    {% error_notifications %}
    <div id=''content-main">

in urls.py::

    import admin_notifications
    admin_notifications.autodiscover()

This looks in each app for a file called 'notifications.py and registers it if it exists.


Notifications files can contain as many functions as you like. Each one should return a string which can contain HTML and each one needs to be registered using admin_notifications.register

If you return an empty string then no notification is shown.

Notifications functions are called every time the admin template is rendered so avoid doing heavy calculations in the notification.

An example notifications.py might look like this::

    import admin_notifications
    from models import Url
    def notification():
        broken_links = Url.objects.filter(status=False).count()
        if broken_links:
            return "You have %s broken link%s.<br>You can view or fix them using the <a href='/admin/linkcheck/'>Link Manager</a>." % (broken_links, "s" if broken_links>1 else "")
        else:
            return ''

    admin_notifications.register(notification)