from django.contrib import admin
from .models import Service, Testimonial, CaseStudy, Resource, BlogPost, FAQ, ProcessStep

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'company', 'content')

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'industry', 'order', 'is_active')
    list_filter = ('is_active', 'industry')
    search_fields = ('title', 'client', 'industry', 'challenge', 'solution', 'results')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'order', 'is_active')
    list_filter = ('is_active', 'resource_type')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'category', 'author', 'is_published')
    list_filter = ('is_published', 'date', 'category')
    search_fields = ('title', 'excerpt', 'content', 'category', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('question', 'answer')

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
