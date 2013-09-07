from apps.accounts.models import DashboardModel
from django import forms
from django.forms import ModelForm


class DashboardForm(ModelForm):
    # date_from = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y'),
    #                             input_formats=('%d/%m/%Y',))
    # date_to = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y'),
    #                           input_formats=('%d/%m/%Y',),
    #                           required=False)

    class Meta:
        model = DashboardModel
        widgets = {
            'date_from': forms.DateInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}, format='%d.%m.%Y'),
            'date_to': forms.DateInput(attrs={'class': 'form-control'}, format='%d.%m.%Y'),
            'country': forms.Select(attrs={'class': 'form-control'})
        }
