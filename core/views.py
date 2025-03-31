from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from django.db import connection
from .models import Service, Testimonial, CaseStudy, Resource, BlogPost, FAQ, ProcessStep

class SafeTemplateView(TemplateView):
    """A TemplateView that handles database errors gracefully."""
    fallback_template = 'fallback.html'
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return render(request, self.fallback_template)
            
    def get_context_data(self, **kwargs):
        try:
            return super().get_context_data(**kwargs)
        except Exception:
            return kwargs

class HomeView(SafeTemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # Check if tables exist
            with connection.cursor() as cursor:
                tables = connection.introspection.table_names()
                if 'core_service' not in tables:
                    return redirect('fallback')
                    
            context['services'] = Service.objects.filter(is_active=True)
            context['testimonials'] = Testimonial.objects.filter(is_active=True)
            context['case_studies'] = CaseStudy.objects.filter(is_active=True)
            context['resources'] = Resource.objects.filter(is_active=True)[:6]
            context['blog_posts'] = BlogPost.objects.filter(is_published=True)[:3]
            context['faqs'] = FAQ.objects.filter(is_active=True)
            context['process_steps'] = ProcessStep.objects.filter(is_active=True)
        except Exception:
            # If any database error occurs, use empty lists
            context['services'] = []
            context['testimonials'] = []
            context['case_studies'] = []
            context['resources'] = []
            context['blog_posts'] = []
            context['faqs'] = []
            context['process_steps'] = []
        return context

class ServiceListView(ListView):
    model = Service
    template_name = 'core/service_list.html'
    context_object_name = 'services'
    queryset = Service.objects.filter(is_active=True)

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'core/service_detail.html'
    context_object_name = 'service'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_service = self.get_object()
        
        # Get related services (exclude current service)
        related_services = Service.objects.filter(
            is_active=True
        ).exclude(
            id=current_service.id
        ).order_by('?')[:3]  # Get 3 random related services
        
        context['related_services'] = related_services
        return context

# Keep the rest of your views as they were...

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)
        context['testimonials'] = Testimonial.objects.filter(is_active=True)
        context['case_studies'] = CaseStudy.objects.filter(is_active=True)
        context['resources'] = Resource.objects.filter(is_active=True)[:6]
        context['blog_posts'] = BlogPost.objects.filter(is_published=True)[:3]
        context['faqs'] = FAQ.objects.filter(is_active=True)
        context['process_steps'] = ProcessStep.objects.filter(is_active=True)
        return context

class ServiceListView(ListView):
    model = Service
    template_name = 'core/service_list.html'
    context_object_name = 'services'
    queryset = Service.objects.filter(is_active=True)

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'core/service_detail.html'
    context_object_name = 'service'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_service = self.get_object()
        
        # Get related services (exclude current service)
        related_services = Service.objects.filter(
            is_active=True
        ).exclude(
            id=current_service.id
        ).order_by('?')[:3]  # Get 3 random related services
        
        context['related_services'] = related_services
        return context
    
class ResourceListView(ListView):
    model = Resource
    template_name = 'core/resource_list.html'
    context_object_name = 'resources'
    
    def get_queryset(self):
        queryset = Resource.objects.filter(is_active=True)
        
        # Filter by resource type if provided in URL parameters
        resource_type = self.request.GET.get('type')
        if resource_type and resource_type != 'all':
            queryset = queryset.filter(resource_type=resource_type)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pass the current filter to the template
        context['current_type'] = self.request.GET.get('type', 'all')
        
        # Get counts for each resource type
        resource_counts = {}
        for resource_type, label in Resource.RESOURCE_TYPES:
            count = Resource.objects.filter(is_active=True, resource_type=resource_type).count()
            if count > 0:
                resource_counts[resource_type] = {'label': label, 'count': count}
        
        context['resource_counts'] = resource_counts
        context['total_count'] = Resource.objects.filter(is_active=True).count()
        
        return context

class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'core/resource_detail.html'
    context_object_name = 'resource'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_resource = self.object
        
        # Get related resources of the same type, excluding the current one
        related_by_type = Resource.objects.filter(
            resource_type=current_resource.resource_type,
            is_active=True
        ).exclude(id=current_resource.id)
        
        # If we don't have enough related resources of the same type, get other types
        if related_by_type.count() < 3:
            other_resources = Resource.objects.filter(is_active=True).exclude(
                id=current_resource.id
            ).exclude(id__in=related_by_type.values_list('id', flat=True))
            related_resources = list(related_by_type) + list(other_resources)
            related_resources = related_resources[:3]
        else:
            related_resources = related_by_type[:3]
        
        context['related_resources'] = related_resources
        return context

class BlogListView(ListView):
    model = BlogPost
    template_name = 'core/blog_list.html'
    context_object_name = 'blog_posts'
    paginate_by = 6
    
    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True).order_by('-date')
        
        # Handle search
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(category__icontains=search_query) |
                Q(tags__icontains=search_query)
            )
            
        # Handle category filtering
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
            
        # Handle tag filtering
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__icontains=tag)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get recent posts for sidebar
        context['recent_posts'] = BlogPost.objects.filter(
            is_published=True
        ).order_by('-date')[:5]
        
        # Get categories with post counts
        categories = {}
        for post in BlogPost.objects.filter(is_published=True):
            if post.category:
                if post.category in categories:
                    categories[post.category] += 1
                else:
                    categories[post.category] = 1
                    
        context['categories'] = [{'name': name, 'count': count} for name, count in categories.items()]
        context['all_posts_count'] = BlogPost.objects.filter(is_published=True).count()
        
        # Get popular tags
        tags = {}
        for post in BlogPost.objects.filter(is_published=True):
            if post.tags:
                for tag in post.tags.split(','):
                    tag = tag.strip()
                    if tag:
                        if tag in tags:
                            tags[tag] += 1
                        else:
                            tags[tag] = 1
                            
        # Sort tags by popularity
        sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
        context['tags'] = [{'name': name, 'count': count} for name, count in sorted_tags[:10]]
        
        return context

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'core/blog_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.get_object()
        
        # Get related posts (posts in the same category or with similar tags)
        related_posts = BlogPost.objects.filter(
            is_published=True
        ).exclude(
            id=current_post.id
        )
        
        # First try to find posts with the same category
        if current_post.category:
            category_matches = related_posts.filter(category=current_post.category)
            if category_matches.exists():
                related_posts = category_matches
                
        # If we have fewer than 3 related posts, get most recent posts instead
        related_posts = related_posts.order_by('-date')[:3]
        context['related_posts'] = related_posts
        
        # Get recent posts for sidebar
        context['recent_posts'] = BlogPost.objects.filter(
            is_published=True
        ).exclude(
            id=current_post.id
        ).order_by('-date')[:5]
        
        # Get categories with post counts for sidebar
        categories = {}
        for post in BlogPost.objects.filter(is_published=True):
            if post.category:
                if post.category in categories:
                    categories[post.category] += 1
                else:
                    categories[post.category] = 1
                    
        context['categories'] = [{'name': name, 'count': count} for name, count in categories.items()]
        
        # Author information
        context['author_image'] = '/static/img/avatar.jpg'  # Default author image
        
        return context

class CaseStudyListView(ListView):
    model = CaseStudy
    template_name = 'core/case_study_list.html'
    context_object_name = 'case_studies'
    queryset = CaseStudy.objects.filter(is_active=True)

class CaseStudyDetailView(DetailView):
    model = CaseStudy
    template_name = 'core/case_study_detail.html'
    context_object_name = 'case_study'
