from django.shortcuts import render
from django.views.generic.base import TemplateView
# https://dowtech.tistory.com/4


class HomeView(TemplateView):
    template_name = 'home.html'


