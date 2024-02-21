from django.contrib import admin
from .models import UniformResourceLocator

class UniformResourceLocatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'shortened_url')
    search_fields = ('original_url', 'shortened_url')

admin.site.register(UniformResourceLocator, UniformResourceLocatorAdmin)
