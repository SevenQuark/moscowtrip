# -*- coding: utf-8 -*-
from apps.accounts.forms import DashboardForm
from django.views.generic import TemplateView
from apps.main.utils import JSONView
from apps.main import placer
from apps.main.models import Place


class PlainTextTemplateView(TemplateView):
    def render_to_response(self, context, **kwargs):
        print 1
        return super(PlainTextTemplateView, self).render_to_response(
            context, content_type='text/plain', **kwargs
        )

    def get_context_data(self, **kwargs):
        form = DashboardForm()
        print form
        return form


class DashboardView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['form'] = DashboardForm()
        return context


class Places(JSONView):
    def get_context_data(self, **kwargs):
        context = super(Places, self).get_context_data(**kwargs)
        context['data'] = placer.places()
        return context
