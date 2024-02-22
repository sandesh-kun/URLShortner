from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import UniformResourceLocator
from .forms import URLForm
from .utils import generate_short_url
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def submit_url(request):
    context = {'form': None, 'error': None, 'submit_disabled': not request.user.is_authenticated}
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to shorten URLs.')
            return redirect('login')
        
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

@login_required
def show_url(request, pk):
    try:
        url_instance = UniformResourceLocator.objects.get(pk=pk)
        short_url = request.build_absolute_uri(f'/{url_instance.shortened_url}/')
    except UniformResourceLocator.DoesNotExist:
        return render(request, 'shortner/error.html', {'error': 'URL not found'})

    return render(request, 'shortner/show.html', {'url_instance': url_instance, 'short_url': short_url})

@login_required 
def redirect_to_original(request, short_url_slug):

    url_instance = get_object_or_404(UniformResourceLocator, shortened_url=short_url_slug)

    return redirect(url_instance.original_url)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Successfully signed up and logged in.')
            return redirect('submit_url') 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            return redirect('submit_url')  
        else:
            
            messages.error(request, 'Username or password is not correct')
            return redirect('login')
    else:
       
        return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('submit_url')