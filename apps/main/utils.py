# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView
import json


class JSONResponseMixin(object):
    """ JSON SBV Mixin """
    def render_to_json_response(self, context, **response_kwargs):
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        return json.dumps(context)


class JSONView(JSONResponseMixin, TemplateView):
    """ JSON SBV вьюха """
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        context.pop('view')
        return self.render_to_json_response(context, **response_kwargs)
