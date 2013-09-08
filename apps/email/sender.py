# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.template import TemplateDoesNotExist, Context, TemplateSyntaxError
from django.template.loader import render_to_string, get_template_from_string
from django.utils.html import strip_tags
import sendgrid
from django.conf import settings
from apps.email import sendgrid_api


def send_email(subject, send_to, template, content_type="plain", message=None,
               send_from=(settings.DEFAULT_FROM_EMAIL, "Moscow Trip Team")):
    if not message: message = {}
    message.update(add_default_context())
    email_content = get_rendered_email_template(template, message)
    if content_type == 'html':
        message = sendgrid.Message(send_from, subject, html=email_content)
    else :
        message = sendgrid.Message(send_from, subject, text=strip_tags(email_content))
    message.add_to(send_to)
    sendgrid_api.web.send(message)


def get_rendered_email_template(template, email_context):
    template_directory = getattr(settings, "EMAIL_TEMPLATE_DIR", 'email')
    if template.endswith('.html') or template.endswith('.txt'):
        try:
            html_content = render_to_string(template_directory+'/%s' % template,email_context)
        except TemplateDoesNotExist:
            raise TemplateDoesNotExist('Template dir %s does not exist.' % template_directory)
    else:
        try:
            t = get_template_from_string(template)
            html_content = t.render(Context(email_context))
        except TemplateSyntaxError:
            raise TemplateSyntaxError('Template syntax error.')
    return html_content


def add_default_context():
    site = Site.objects.get_current()
    return {"site":{'sitename': site.name,'domain':site.domain}}

# send_email(subject="Your plan from Moscow Trip",send_to='kexbit@gmail.com',content_type='html', template="plan.html")