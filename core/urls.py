from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'core'

urlpatterns = [
    # Main views using the fixed HomeView with fallback
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('resources/', views.ResourceListView.as_view(), name='resource_list'),
    path('resources/<slug:slug>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('case-studies/', views.CaseStudyListView.as_view(), name='case_study_list'),
    path('case-studies/<slug:slug>/', views.CaseStudyDetailView.as_view(), name='case_study_detail'),
    
    # Direct fallback for testing
    path('fallback/', TemplateView.as_view(template_name='fallback.html'), name='fallback'),
    path('starter/', TemplateView.as_view(template_name='starter.html'), name='starter'),
]