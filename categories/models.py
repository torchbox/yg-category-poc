from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable

from .widgets import VirtualTypeChooser


class CategoryPage(Page):
    short_name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('short_name'),
        InlinePanel('assigned_virtual_types', label="Assigned virtual types"),
    ]


class CategoryAssignedVirtualType(Orderable):
    page = ParentalKey(CategoryPage, on_delete=models.CASCADE, related_name='assigned_virtual_types')
    virtual_type_id = models.CharField(max_length=255)

    panels = [
        FieldPanel('virtual_type_id', widget=VirtualTypeChooser),
    ]
