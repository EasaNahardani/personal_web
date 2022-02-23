from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home , name='home'),
    path(_('contact/'), views.contact , name='contact'),
    path(_('about/'), views.about , name='about'),
    path(_('education/'), views.education , name='education'),
    path(_('skills/'), views.skills , name='skills'),
    path(_('projects/'), views.projects , name='projects'),
]
