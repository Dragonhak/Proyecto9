from django.shortcuts          import render
from django.views.generic.base import TemplateView

# Vista basa en clases
class home(TemplateView):
	template_name = "home/home.html"

	def get_context_data(self, **kwargs):
		context = super(home, self).get_context_data(**kwargs)
		return context