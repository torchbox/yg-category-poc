from generic_chooser.widgets import DRFChooser

class VirtualTypeChooser(DRFChooser):
    choose_modal_url_name = 'virtual_type_chooser:choose'
    api_base_url = 'https://yougov.co.uk/_pubapis/v5/uk/entities/virtual_types/'

    #def get_title(self, instance):
    #    return instance['title']
