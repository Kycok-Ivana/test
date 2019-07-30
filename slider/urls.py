from django.urls import path
from .views import by_slider
from django.views.generic import TemplateView
urlpatterns = [
    path ('', by_slider),
]