from django.core.exceptions import ObjectDoesNotExist
import requests
from generic_chooser.widgets import DRFChooser

class StaticAPIChooser(DRFChooser):

    def get_title(self, instance):
        return instance[self.name_field]

    def get_object_list(self):
        result = requests.get(self.api_base_url).json()
        return result

    def get_instance(self, id):
        object_list = self.get_object_list()
        for item in object_list:
            if item['uuid'] == id:
                return item

        raise ObjectDoesNotExist()


class VirtualTypeChooser(StaticAPIChooser):
    choose_modal_url_name = 'virtual_type_chooser:choose'
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/entities/virtual_types/'
    name_field = 'name'


class TrackerChooser(StaticAPIChooser):
    choose_modal_url_name = 'tracker_chooser:choose'
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/trackers/list/'
    name_field = 'title'
