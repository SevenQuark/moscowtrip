from apps.accounts.models import DashboardModel
from django.forms import ModelForm


class DashboardForm(ModelForm):
    class Meta:
        model = DashboardModel