from django.core.exceptions import ObjectDoesNotExist
import requests
from generic_chooser.widgets import DRFChooser

class VirtualTypeChooser(DRFChooser):
    choose_modal_url_name = 'virtual_type_chooser:choose'
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/entities/virtual_types/'

    def get_title(self, instance):
        return instance['name']

    def get_object_list(self):
        result = requests.get(self.api_base_url).json()
        return result

    def get_instance(self, id):
        object_list = self.get_object_list()
        for item in object_list:
            if item['uuid'] == id:
                return item

        raise ObjectDoesNotExist()
