from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    # Use direct template view to avoid any database access
    path('', TemplateView.as_view(template_name='starter.html'), name='home'),
]