from django import forms
from .models import UniformResourceLocator

class URLForm(forms.ModelForm):
    class Meta:
        model = UniformResourceLocator
        fields = ['original_url']