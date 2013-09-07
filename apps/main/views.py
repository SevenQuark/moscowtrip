# -*- coding: utf-8 -*-
from apps.accounts.forms import DashboardForm
from apps.accounts.models import DashboardModel
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from apps.main.utils import JSONView
from apps.main import placer


class PlainTextTemplateView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(PlainTextTemplateView, self).render_to_response(
            context, content_type='text/plain', **kwargs
        )

    def get_context_data(self, **kwargs):
        form = DashboardForm()
        return form


class DashboardCreateView(CreateView):

    template_name = "index.html"
    form_class = DashboardForm
    model = DashboardModel

    def get_success_url(self):
        return reverse('dashboard:view',kwargs={'db_id':self.object.hash})

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())



class Places(JSONView):
    def get_context_data(self, **kwargs):
        context = super(Places, self).get_context_data(**kwargs)
        context['data'] = placer.get_places()
        return context
