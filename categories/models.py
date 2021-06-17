from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable

from .widgets import TrackerChooser, VirtualTypeChooser


class CategoryPage(Page):
    short_name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('short_name'),
        InlinePanel('virtual_types', label="Virtual types"),
        InlinePanel('trackers', label="Trackers"),
    ]


class CategoryVirtualType(Orderable):
    page = ParentalKey(CategoryPage, on_delete=models.CASCADE, related_name='virtual_types')
    virtual_type_id = models.CharField(max_length=255)
    is_promoted = models.BooleanField(blank=True)

    panels = [
        FieldPanel('virtual_type_id', widget=VirtualTypeChooser()),
        FieldPanel('is_promoted'),
    ]


class CategoryTracker(Orderable):
    page = ParentalKey(CategoryPage, on_delete=models.CASCADE, related_name='trackers')
    tracker_id = models.CharField(max_length=255)
    is_promoted = models.BooleanField(blank=True)

    panels = [
        FieldPanel('tracker_id', widget=TrackerChooser()),
        FieldPanel('is_promoted'),
    ]
