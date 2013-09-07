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
    date_from = models.DateTimeField(default=lambda: datetime.date.today - datetime.timedelta(days=-3))
    date_to = models.DateField(default=datetime.date.today)
    country = CountryField()