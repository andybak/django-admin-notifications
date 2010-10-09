import imp
import os

_error_registry = []
_alert_registry = []
_app_block_registry = []

def register(notifications):
    if type(notifications).__name__=='function':
         # for compatibility we assume that registering a single function is an error notification
        _error_registry.append(notifications)
    else:
        switch = {
            'errors': _error_registry,
            'alerts': _alert_registry,
            'app_blocks': _app_block_registry,
        }
        for ntype in notifications.keys():
            action = switch[ntype]
            for entry in notifications[ntype]:
                action.append(entry)

def autodiscover():
    from django.conf import settings
    for app in settings.INSTALLED_APPS:
        try:
            app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
        except AttributeError:
            continue
        try:
            imp.find_module('notifications', app_path)
        except ImportError:
            continue
        __import__("%s.notifications" % app)


