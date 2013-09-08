import hashlib
import time
from apps.accounts.models import DashboardModel
from django import forms
from django.forms import ModelForm


class DashboardForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DashboardForm, self).__init__(*args, **kwargs)
        self.fields['date_from'].input_formats = ['%m.%d.%Y']
        self.fields['date_to'].input_formats = ['%m.%d.%Y']


    class Meta:
        model = DashboardModel
        widgets = {
            'date_from': forms.DateInput(attrs={'class': 'form-control', 'autofocus': 'autofocus','placeholder':'Date from', 'autocomplete':'off'   }, format='%d.%m.%Y'),
            'date_to': forms.DateInput(attrs={'class': 'form-control','placeholder':'Date to', 'autocomplete':'off'}, format='%d.%m.%Y',),
        }
        exclude = ('country',)

    def save(self, commit=True):
        form_model = super(DashboardForm, self).save(commit=commit)
        m = hashlib.md5()
        m.update(str(time.time()))
        form_model.hash = m.hexdigest()
        form_model.save()
        return form_model
