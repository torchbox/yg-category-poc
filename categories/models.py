from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable

from .widgets import TrackerChooser, VirtualTypeChooser


class CategoryPage(Page):
    short_name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('short_name'),
        InlinePanel('assigned_virtual_types', label="Assigned virtual types"),
        InlinePanel('promoted_virtual_types', label="Promoted virtual types"),
        InlinePanel('trackers', label="Trackers"),
    ]


class CategoryAssignedVirtualType(Orderable):
    page = ParentalKey(CategoryPage, on_delete=models.CASCADE, related_name='assigned_virtual_types')
    virtual_type_id = models.CharField(max_length=255)

    panels = [
        FieldPanel('virtual_type_id', widget=VirtualTypeChooser),
    ]


class CategoryPromotedVirtualType(Orderable):
    page = ParentalKey(CategoryPage, on_delete=models.CASCADE, related_name='promoted_virtual_types')
    virtual_type_id = models.CharField(max_length=255)

    panels = [
        FieldPanel('virtual_type_id', widget=VirtualTypeChooser),
    ]


class CategoryTracker(Orderable):
    page = ParentalKey(CategoryPage, on_delete=models.CASCADE, related_name='trackers')
    tracker_id = models.CharField(max_length=255)
    is_promoted = models.BooleanField(blank=True)

    panels = [
        FieldPanel('tracker_id', widget=TrackerChooser),
        FieldPanel('is_promoted'),
    ]
