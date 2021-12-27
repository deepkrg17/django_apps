from django.urls import path
from . import views

urlpatterns = [
    path('<int:num>/', views.home, name='home'),
    path('api/<int:num>/', views.api, name='api')
    ]