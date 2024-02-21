from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import UniformResourceLocator
from .forms import URLForm
from .utils import generate_short_url

def submit_url(request):
    context = {'form': None, 'error': None}
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            submitted_url = form.cleaned_data['original_url']
            try:
                unique_short_url = generate_short_url()
                new_url_instance = UniformResourceLocator(
                    original_url=submitted_url,
                    shortened_url=unique_short_url
                )
                new_url_instance.save()

                return redirect('show_short_url', pk=new_url_instance.pk)
            except IntegrityError:
                context['error'] = 'Failed to generate a unique short URL. Please try again.'
        else:
            context['error'] = 'Form is not valid. Please check your input.'
    else:
        form = URLForm()
    
    context['form'] = form
    return render(request, 'shortner/submit.html', context)

def show_url(request, pk):
    try:
        url_instance = UniformResourceLocator.objects.get(pk=pk)
        short_url = request.build_absolute_uri(f'/{url_instance.shortened_url}/')
    except UniformResourceLocator.DoesNotExist:
        return render(request, 'shortner/error.html', {'error': 'URL not found'})

    return render(request, 'shortner/show.html', {'url_instance': url_instance, 'short_url': short_url})

def redirect_to_original(request, short_url_slug):

    url_instance = get_object_or_404(UniformResourceLocator, shortened_url=short_url_slug)

    return redirect(url_instance.original_url)