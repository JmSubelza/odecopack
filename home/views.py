from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class HomeView(View):
    template_name = "listasprecios/emails/cotizacion.html"
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)



