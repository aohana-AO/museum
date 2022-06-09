from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Item

class IndexView(LoginRequiredMixin,TemplateView):
    template_name='app/index.html'



