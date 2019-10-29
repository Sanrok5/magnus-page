from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index


class HomePage(Page):
    pass
    ventas_contado = RichTextField(blank=True, features=['h4', 'h5', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed', 'code', 'superscript', 'blockquote'])
    ventas_contado_entes = RichTextField(blank=True)
    ventas_contado_documentos = RichTextField(blank=True)
    ventas_contado_flujo = RichTextField(blank=True)
    ventas_contado_valores = RichTextField(blank=True)
    ventas_contado_tiempos = RichTextField(blank=True)
    ventas_contado_alcances = RichTextField(blank=True)
    ventas_contado_pagos = RichTextField(blank=True)

    ventas_subsidio = RichTextField(blank=True)
    ventas_subsidio_entes = RichTextField(blank=True)
    ventas_subsidio_documentos = RichTextField(blank=True)
    ventas_subsidio_flujo = RichTextField(blank=True)
    ventas_subsidio_valores = RichTextField(blank=True)
    ventas_subsidio_tiempos = RichTextField(blank=True)
    ventas_subsidio_alcances = RichTextField(blank=True)
    ventas_subsidio_pagos = RichTextField(blank=True)

    ventas_credito = RichTextField(blank=True)
    ventas_mixto = RichTextField(blank=True)

    arriendos_documentos = RichTextField(blank=True)
    arriendos_subsidios = RichTextField(blank=True)
    arriendos_contrato = RichTextField(blank=True)

    info_subsidios = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('ventas_contado', classname="full"),
            FieldPanel('ventas_contado_entes', classname="full"),
            FieldPanel('ventas_contado_documentos', classname="full"),
            FieldPanel('ventas_contado_flujo', classname="full"),
            FieldPanel('ventas_contado_valores', classname="full"),
            FieldPanel('ventas_contado_tiempos', classname="full"),
            FieldPanel('ventas_contado_alcances', classname="full"),
            FieldPanel('ventas_contado_pagos', classname="full"),
        ], heading="Ventas Contado"),
        MultiFieldPanel([
            FieldPanel('ventas_subsidio', classname="full"),
            FieldPanel('ventas_subsidio_entes', classname="full"),
            FieldPanel('ventas_subsidio_documentos', classname="full"),
            FieldPanel('ventas_subsidio_flujo', classname="full"),
            FieldPanel('ventas_subsidio_valores', classname="full"),
            FieldPanel('ventas_subsidio_tiempos', classname="full"),
            FieldPanel('ventas_subsidio_alcances', classname="full"),
            FieldPanel('ventas_subsidio_pagos', classname="full"),
        ], heading="Ventas Subsidio"),
        MultiFieldPanel([
            FieldPanel('arriendos_documentos', classname="full"),
            FieldPanel('arriendos_subsidios', classname="full"),
            FieldPanel('arriendos_contrato', classname="full"),
        ], heading="Arriendos"),
        MultiFieldPanel([
            FieldPanel('info_subsidios', classname="full"),
        ], heading="Información de los subsidios"),
    ]
