from wagtail.core import hooks

from categories.views import TrackerChooserViewSet, VirtualTypeChooserViewSet


@hooks.register('register_admin_viewset')
def register_virtual_type_chooser_viewset():
    return VirtualTypeChooserViewSet('virtual_type_chooser', url_prefix='virtual-type-chooser')


@hooks.register('register_admin_viewset')
def register_tracker_chooser_viewset():
    return TrackerChooserViewSet('tracker_chooser', url_prefix='tracker-chooser')
