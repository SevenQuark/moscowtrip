from apps.accounts.views import DashboardView
from django.conf.urls import patterns, url


urlpatterns = patterns('',
       url(r'^(?P<db_id>\w+)/$', DashboardView.as_view(), name="view")
)
