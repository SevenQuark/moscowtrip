from apps.main.views import PlainTextTemplateView, PayPal, DashboardCreateView, SavePlanView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.main.views import Places
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', DashboardCreateView.as_view()),
    url(r'^robots\.txt$', PlainTextTemplateView.as_view(template_name='robots.txt')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^places/', Places.as_view()),
    url(r'^paypal/(?P<client_id>.*)/', PayPal.as_view()),
    url(r'^paypal_complate/', PayPalComplete.as_view()),
    (r'^dashboard/', include('apps.accounts.urls', namespace = 'dashboard')),
    (r'^complete/', TemplateView.as_view(template_name='purchase/complete.html')),
    url(r'^get_plan/', SavePlanView.as_view()),
    (r'^dashboard/', include('apps.accounts.urls', namespace = 'dashboard'))
)
