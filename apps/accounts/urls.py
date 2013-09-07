from apps.accounts.views import DashboardView
from django.conf.urls import patterns, url


urlpatterns = patterns('',
       url(r'^$', DashboardView.as_view(), name="view")
)
