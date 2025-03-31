from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., 'fas fa-bullseye')")
    short_description = models.TextField(max_length=500)
    full_description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', 'title']

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.company}"
    
    @classmethod
    def create_or_update(cls, name, position, company, content, image=None, order=0):
        """Create or update a testimonial with the given data"""
        testimonial, created = cls.objects.get_or_create(
            name=name,
            company=company,
            defaults={
                'position': position,
                'content': content,
                'order': order,
                'is_active': True
            }
        )
        
        if not created:
            testimonial.position = position
            testimonial.content = content
            testimonial.order = order
            testimonial.save()
            
        if image and not testimonial.image:
            testimonial.image = image
            testimonial.save()
            
        return testimonial
    
    class Meta:
        ordering = ['order', 'name']

class CaseStudy(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    client = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    challenge = models.TextField()
    solution = models.TextField()
    results = models.TextField()
    result_metrics = models.JSONField(null=True, blank=True, help_text="Store key metrics as a JSON object")
    image = models.ImageField(upload_to='case_studies/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('case_study_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name_plural = "Case Studies"

class Resource(models.Model):
    RESOURCE_TYPES = (
        ('guide', 'Guide'),
        ('template', 'Template'),
        ('ebook', 'E-Book'),
        ('checklist', 'Checklist'),
        ('tool', 'Tool'),
        ('framework', 'Framework'),
    )
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class")
    short_description = models.TextField(max_length=500)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='resources/thumbnails/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', 'title']

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(max_length=500)
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    author = models.CharField(max_length=100, default="Amit Bhalla")
    read_time = models.PositiveIntegerField(default=5, help_text="Estimated reading time in minutes")
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    date = models.DateField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date', 'title']

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

class ProcessStep(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
