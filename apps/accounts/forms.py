from apps.accounts.models import DashboardModel
from django import forms
from django.forms import ModelForm


class DashboardForm(ModelForm):

    class Meta:
        model = DashboardModel
        widgets = {
            'date_from': forms.DateInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}, format='%d.%m.%Y'),
            'date_to': forms.DateInput(attrs={'class': 'form-control'}, format='%d.%m.%Y'),
            'country': forms.Select(attrs={'class': 'form-control'})
        }
