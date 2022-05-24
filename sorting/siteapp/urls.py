from django.urls import path
from django.views.generic import TemplateView
from siteapp.views import main_view

urlpatterns = [
    path('', main_view, name='main'),
    path('result/', TemplateView.as_view(template_name='result.html'), name='result'),
]
