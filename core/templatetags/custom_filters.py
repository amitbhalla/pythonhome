from django import template
from django.utils.safestring import mark_safe
import markdown
import bleach

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def markdown_to_html(text):
    """Converts markdown text to safe HTML"""
    if not text:
        return ''
    
    # Convert markdown to HTML
    html = markdown.markdown(
        text,
        extensions=['markdown.extensions.fenced_code', 'markdown.extensions.tables', 'markdown.extensions.nl2br']
    )
    
    # List of allowed HTML tags and attributes for security
    allowed_tags = [
        'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'abbr', 'acronym', 'b', 'blockquote',
        'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'br', 'hr', 'div', 'span', 'table',
        'thead', 'tbody', 'tr', 'th', 'td', 'img', 'pre', 'sup', 'sub'
    ]
    
    allowed_attrs = {
        '*': ['class', 'id', 'style'],
        'a': ['href', 'title', 'target', 'rel'],
        'img': ['src', 'alt', 'title', 'width', 'height']
    }
    
    # Clean the HTML to prevent XSS attacks
    clean_html = bleach.clean(html, tags=allowed_tags, attributes=allowed_attrs)
    
    # Mark the HTML as safe to prevent Django from escaping it
    return mark_safe(clean_html)
