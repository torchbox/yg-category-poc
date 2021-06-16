from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
import requests

from generic_chooser.views import DRFChooserMixin, DRFChooserViewSet

class VirtualTypeChooserMixin(DRFChooserMixin):
    def get_object_list(self, **kwargs):
        params = self.get_api_parameters(**kwargs)
        result = requests.get(self.api_base_url, params=params).json()
        return result

    def get_object_id(self, item):
        return item['uuid']

    def get_object_string(self, item):
        return item['name']


class VirtualTypeChooserViewSet(DRFChooserViewSet):
    # base_choose_view_class = VirtualTypeChooseView
    chooser_mixin_class = VirtualTypeChooserMixin
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/entities/virtual_types/'

    def get_urlpatterns(self):
        return super().get_urlpatterns() + [
            url(r'^$', self.choose_view, name='choose'),
            url(r'^([\w\-]+)/$', self.chosen_view, name='chosen'),
        ]
