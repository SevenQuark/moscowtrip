# -*- coding: utf-8 -*-
import datetime
from apps.accounts.forms import DashboardForm
from apps.accounts.models import DashboardModel
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from apps.main.utils import JSONView
from apps.main import placer
from apps.main.models import Place
from apps.instagram_api.data_driver import get_norm_activities_by_days


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

        category = self.request.GET.get('category', 'museum,').split(',')
        congestion = int(self.request.GET.get('congestion', 0))
        dm = int(self.request.GET.get('dm', 1))

        asd = get_norm_activities_by_days()

        p1 = []
        p2 = []
        p3 = []
        for a in asd:
            p = Place.objects.get(place_id=a['fid'])
            con = a['days'][dm - 1]
            days_full =  a['days_full'][dm - 1]
            if p.category in category:
                if con == 1 and congestion in [1, 2, 3, 0]:
                    p1.append(dict(
                        category=p.category,
                        days_full=days_full,
                        data=p.data
                    ))
                if con == 2 and congestion in [2, 3, 0]:
                    p2.append(dict(
                        category=p.category,
                        days_full=days_full,
                        data=p.data
                    ))
                if con == 3 and congestion in [3, 0]:
                    p3.append(dict(
                        category=p.category,
                        days_full=days_full,
                        data=p.data
                    ))

        context['p1'] = p1
        context['p2'] = p2
        context['p3'] = p3

        return context
