# posts/views.py
from django.views.generic import ListView
from .models import post

class HomePageView(ListView):
    model = post
    template_name = "home.html"
