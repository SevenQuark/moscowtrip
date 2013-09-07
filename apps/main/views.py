from django.views.generic import TemplateView


class PlainTextTemplateView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(PlainTextTemplateView, self).render_to_response(
            context, content_type='text/plain', **kwargs
        )
