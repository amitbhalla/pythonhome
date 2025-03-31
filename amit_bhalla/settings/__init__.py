"""
Settings package initialization.
This file determines which settings to load based on the environment.
"""
import os

# Load the appropriate settings based on the DJANGO_SETTINGS_MODULE environment variable
# If not set, default to local settings
settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings.local')

if settings_module == 'amit_bhalla.settings.production':
    from .production import *
else:
    from .local import *
