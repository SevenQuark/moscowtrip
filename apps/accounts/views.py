# Create your views here.
from apps.accounts.models import DashboardModel
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView,self).get_context_data(**kwargs)
        db = DashboardModel.objects.get(hash=kwargs.get('db_id'))
        context.update({'dashboard':db})
        return context