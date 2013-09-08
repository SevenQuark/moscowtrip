import datetime
from django.utils.translation import ugettext as _
from auth_pack.models import AbstractEmailUser
from django.db import models
from django_countries import CountryField


class User(AbstractEmailUser):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class DashboardModel(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    country = CountryField(null=True)
    hash = models.CharField(max_length=32, blank=True)
    email = models.CharField(blank=True, max_length=200)
    data = models.TextField(blank=True)


    def format_date_from(self, obj):
        return obj.date.strftime('%m.%d.%Y')

    def format_date_to(self, obj):
        return obj.date.strftime('%m.%d.%Y')

    @property
    def dates(self):
        day = self.date_to.day - self.date_from.day
        return [ self.date_from + datetime.timedelta(days=x) for x in range(0,day+1) ]