from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home , name='home'),
    path('contact/', views.contact , name='contact'),
    path('about/', views.about , name='about'),
    path('education/', views.education , name='education'),
]
