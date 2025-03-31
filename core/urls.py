from django.urls import path
from django.views.generic import TemplateView
from . import views
from . import views_debug

# Import the updated HomeView with error handling
try:
    from .views_updated import HomeView
except ImportError:
    # Fallback if import fails
    HomeView = TemplateView.as_view(template_name='fallback.html')

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('resources/', views.ResourceListView.as_view(), name='resource_list'),
    path('resources/<slug:slug>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('case-studies/', views.CaseStudyListView.as_view(), name='case_study_list'),
    path('case-studies/<slug:slug>/', views.CaseStudyDetailView.as_view(), name='case_study_detail'),
    
    # Debug URL - only works when DEBUG=True
    path('debug/', views_debug.debug_info, name='debug_info'),
    
    # Fallback path for when everything else fails
    path('fallback/', TemplateView.as_view(template_name='fallback.html'), name='fallback'),
]