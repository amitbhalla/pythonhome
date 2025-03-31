"""
URL configuration for amit_bhalla project.
Simplified for direct rendering.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# This is an emergency URL configuration that doesn't rely on complex views
urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Direct fallback views for testing
    path("starter/", TemplateView.as_view(template_name='starter.html'), name='starter'),
    path("fallback/", TemplateView.as_view(template_name='fallback.html'), name='fallback'),
    
    # Include the core URLs if they work
    path("", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)