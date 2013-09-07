import datetime
from django.utils.translation import ugettext as _
from auth_pack.models import AbstractEmailUser
from django.db import models


class User(AbstractEmailUser):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class DashboardModel(models.Model):
    date_from = models.DateTimeField(default=lambda: datetime.datetime.now() - datetime.timedelta(days=-3))
    date_to = models.DateTimeField(default=datetime.datetime.now)
    location_from = models.CharField(max_length=255)