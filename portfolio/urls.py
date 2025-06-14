from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_uid, name='generate_uid'),

    path('portfolio/<uuid:uid>/', views.home, name='portfolio_home'),  # <-- Add this if needed

    path('home/<uuid:uid>/', views.home, name='home'),
    path('profile/<uuid:uid>/', views.profile, name='profile'),
    path('projects/<uuid:uid>/', views.projects, name='projects'),
    path('achievements/<uuid:uid>/', views.achievements, name='achievements'),
    path('contact/<uuid:uid>/', views.contact, name='contact'),

    path('home/', views.redirect_with_uid, {'page': 'home'}),
    path('profile/', views.redirect_with_uid, {'page': 'profile'}),
    path('projects/', views.redirect_with_uid, {'page': 'projects'}),
    path('achievements/', views.redirect_with_uid, {'page': 'achievements'}),
    path('contact/', views.redirect_with_uid, {'page': 'contact'}),
]
