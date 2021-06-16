from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from categories.models import CategoryPage

class ArticlePage(Page):

    # Fields and Meta
    # ********************************************************
    primary_category = ParentalKey(
        CategoryPage,
        verbose_name=_("Primary category"),
        null=True,
        on_delete=models.SET_NULL,
    )
    secondary_categories = ParentalManyToManyField(
        CategoryPage,
        verbose_name=_("Secondary categories"),
        blank=True,
        related_name="+",
    )

    content = StreamField(
        [
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ],
        verbose_name=_("Content")
    )

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    # Attributes
    # ********************************************************
    subpage_types = []
    search_fields = Page.search_fields + [index.SearchField("content")]

    # Methods
    # ********************************************************
    @property
    def categories(self) -> list:
        """
        Get all categories for this article, with the primary category at the front.
        """
        if self.primary_category:
            return [
                self.primary_category,
                *self.secondary_categories.exclude(id=self.primary_category.id)
            ]

        return [*self.secondary_categories.all()]

    # Panels
    # ********************************************************
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('primary_category'),
                FieldPanel('secondary_categories'),
            ],
            _("Categories")
        ),
        StreamFieldPanel('content'),
    ]
