from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='test-home'),
    path('about/', views.about, name='test-about'),

]