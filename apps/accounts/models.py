from django.utils.translation import ugettext as _
from auth_pack.models import AbstractEmailUser


class User(AbstractEmailUser):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
