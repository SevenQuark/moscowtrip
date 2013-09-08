# -*- coding: utf-8 -*-
import sendgrid
from django.conf import settings

sendgrid_config = getattr(settings,"SENDGRID_SETTINGS",{})

sendgrid_api = sendgrid.Sendgrid(**sendgrid_config)

