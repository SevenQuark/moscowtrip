# -*- coding: utf-8 -*-
import datetime
import json
from apps.accounts.forms import DashboardForm
from apps.accounts.models import DashboardModel
from apps.email.sender import send_email
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, View, FormView
from apps.main.utils import JSONView
from apps.main import placer
from apps.main.models import Place
from apps.instagram_api.data_driver import get_norm_activities_by_days
from django import http
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.http import HttpResponse


class PlainTextTemplateView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(PlainTextTemplateView, self).render_to_response(
            context, content_type='text/plain', **kwargs
        )

    def get_context_data(self, **kwargs):
        form = DashboardForm()
        return form


class PayPal(View):
    def post(self, request, client_id):
        print(request.POST)
        print(client_id)
        receiver_email = self.request.POST['receiver_email']
        payment_status = self.request.POST['payment_status']

        if payment_status and payment_status[0] == 'Completed':
            # SEND MAIL to receiver_email
            db =  DashboardModel.objects.get(hash=client_id)
            send_email(message=json.loads(db.data), subject="Your plan from Moscow Trip",send_to=db.email,content_type='html', template="plan.html")
        return HttpResponse('Ok')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PayPal, self).dispatch(*args, **kwargs)


class PayPalComplete(View):
    def post(self, request):
        return http.HttpResponseRedirect('/complete/')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PayPalComplete, self).dispatch(*args, **kwargs)



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


class SavePlanView(View):
    def post(self, request):
        data = json.loads(request.POST.get('data'))
        print data
        mail = data['email']
        google_map_url = 'http://maps.googleapis.com/maps/api/staticmap?size=600x300&sensor=false&zoom=13&markers=color:red%7Ccolor:red%7Clabel:C%7C'
        res = []
        for d in data['fidsday']:
            place = Place.objects.get(place_id=d[0])
            obj = {'fid': d[0], 'date': datetime.datetime.strptime(d[1], '%m-%d-%Y'), 'data': place.data}
            url = google_map_url + str(obj['data']['location']['lat']) + ',' + str(obj['data']['location']['lng'])
            obj['map_url'] = url
            res.append(obj)

        json_data = json.dumps(res)


        print res
