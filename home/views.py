from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    
class AuthorizeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'