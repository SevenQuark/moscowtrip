from apps.accounts.models import DashboardModel
from django import forms
from django.forms import ModelForm


class DashboardForm(ModelForm):
    class Meta:
        model = DashboardModel
        widgets = {
            'date_from': forms.TextInput(attrs={'class':'form-control','autofocus':'autofocus'}),
            'date_to': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'})
        }