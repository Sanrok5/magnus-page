from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index


class HomePage(Page):
    pass
    ventas_contado = RichTextField(blank=True)
    ventas_subsidio = RichTextField(blank=True)
    ventas_credito = RichTextField(blank=True)
    ventas_mixto = RichTextField(blank=True)

    arriendos_documentos = RichTextField(blank=True)
    arriendos_subsidios = RichTextField(blank=True)
    arriendos_contrato = RichTextField(blank=True)

    info_subsidios = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('ventas_contado', classname="full"),
            FieldPanel('ventas_subsidio', classname="full"),
            FieldPanel('ventas_credito', classname="full"),
            FieldPanel('ventas_mixto', classname="full"),
        ], heading="Ventas"),
        MultiFieldPanel([
            FieldPanel('arriendos_documentos', classname="full"),
            FieldPanel('arriendos_subsidios', classname="full"),
            FieldPanel('arriendos_contrato', classname="full"),
        ], heading="Arriendos"),
        MultiFieldPanel([
            FieldPanel('info_subsidios', classname="full"),
        ], heading="Información de los subsidios"),
    ]
