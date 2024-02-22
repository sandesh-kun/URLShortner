from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', views.submit_url, name='submit_url'),
    path('show/<int:pk>/', views.show_url, name='show_short_url'),
    path('<slug:short_url_slug>/', views.redirect_to_original, name='redirect_to_original'),
    
]
