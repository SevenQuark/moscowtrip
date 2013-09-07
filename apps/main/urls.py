from apps.main.views import PlainTextTemplateView
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^robots\.txt$', PlainTextTemplateView.as_view(template_name='robots.txt')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^dashboard/', include('apps.accounts.urls', namespace = 'dashboard'))
)
