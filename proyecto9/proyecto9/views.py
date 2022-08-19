from re import template
from django.shortcuts          import render
from django.views.generic.base import TemplateView

# Vista basa en clases
class home(TemplateView):
	template_name = "home/home.html"

	def get_context_data(self, **kwargs):
		context = super(home, self).get_context_data(**kwargs)
		return context
class Error404View(TemplateView):
	template_name= "error_404.html"

class Error500View(TemplateView):
	template_name= "error_404.html"

	@classmethod
	def as_error_view(cls):

		v = cls.as_view()
		def view(request):
			r = v(request)
			r.render()
			return r
		return view
