"""Обработчики URL запросов."""
from django.views.generic.base import TemplateView


class AboutSiteView(TemplateView):
    template_name = 'about/about_site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['text'] = 'Описание сайта'
        return context
