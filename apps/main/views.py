# -*- coding: utf-8 -*-
from apps.accounts.forms import DashboardForm
from apps.accounts.models import DashboardModel
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from apps.main.utils import JSONView
from apps.main import placer
from apps.main.models import Place


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
        category = self.request.GET.get('category', 'museum,').split(',')
        congestion = int(self.request.GET.get('congestion', 0))
        dm = int(self.request.GET.get('dm', 1))

        context = super(Places, self).get_context_data(**kwargs)
        places = Place.objects.filter(category__in=category)
        result = []
        for p in places:
            result.append(dict(
                category=p.category,
                data=p.data
            ))

        if congestion in [0, 1]:
            context['p1'] = result[:30]

        if congestion in [0, 2]:
            context['p1'] = result[:30]
            context['p2'] = result[30:60]

        if congestion in [0, 3]:
            context['p1'] = result[:30]
            context['p2'] = result[30:60]
            context['p3'] = result[60:]

        return context
