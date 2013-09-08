from apps.main.views import PlainTextTemplateView, PayPal, DashboardCreateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.main.views import Places


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', DashboardCreateView.as_view()),
    url(r'^robots\.txt$', PlainTextTemplateView.as_view(template_name='robots.txt')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^places/', Places.as_view()),
    url(r'^paypal/', PayPal.as_view()),
    (r'^dashboard/', include('apps.accounts.urls', namespace = 'dashboard'))
)
