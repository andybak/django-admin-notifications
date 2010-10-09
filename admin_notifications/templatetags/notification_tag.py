from django import template

from linkcheck.models import Url

register = template.Library()

@register.inclusion_tag('admin_error_notifications.html')
def error_notifications():
    from admin_notifications import _error_registry
    notifications = [x for x in [x() for x in _error_registry] if x]
    return {
        'notifications': notifications,
    }
    

@register.simple_tag
def app_block(app):
    from admin_notifications import _app_block_registry
    html = u''
    for tuple in _app_block_registry:
        if tuple[0].lower()==app['name'].lower():
            html += u'\n'.join(["<tr><th scope='row' colspan='3'>%s</th></tr>" % x() for x in tuple[1:]])
    return html