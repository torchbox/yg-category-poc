from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
import requests

from generic_chooser.views import DRFChooserMixin, DRFChooserViewSet

class StaticAPIChooserMixin(DRFChooserMixin):
    def get_object_list(self, search_term=None, **kwargs):
        result = requests.get(self.api_base_url).json()
        if search_term:
            result = [
                item for item in result
                if search_term in item[self.name_field]
            ]

        return result

    def get_object_id(self, item):
        return item['uuid']

    def get_object_string(self, item):
        return item[self.name_field]

    def get_object(self, id):
        object_list = self.get_object_list()
        for item in object_list:
            if item['uuid'] == id:
                return item

        raise ObjectDoesNotExist()


class VirtualTypeChooserMixin(StaticAPIChooserMixin):
    name_field = 'name'


class TrackerChooserMixin(StaticAPIChooserMixin):
    name_field = 'title'


class StaticAPIChooserViewSet(DRFChooserViewSet):
    is_searchable = True

    def get_urlpatterns(self):
        return super().get_urlpatterns() + [
            url(r'^$', self.choose_view, name='choose'),
            url(r'^([\w\-]+)/$', self.chosen_view, name='chosen'),
        ]


class VirtualTypeChooserViewSet(StaticAPIChooserViewSet):
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/entities/virtual_types/'
    chooser_mixin_class = VirtualTypeChooserMixin


class TrackerChooserViewSet(StaticAPIChooserViewSet):
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/trackers/list/'
    chooser_mixin_class = TrackerChooserMixin
