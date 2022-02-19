from django.shortcuts import render
from .models import Skill, Mobile


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def home(request):
    return render(request, './app/home.html')


def contact(request):
    return render(request, './app/contact.html')


def about(request):
    return render(request, './app/about.html')


def education(request):
    return render(request, './app/education.html')


def skills(request):
    skills = Skill.objects.all()
    return render(request, './app/skills.html', {'skills':skills})


def projects(request):
    if is_ajax(request):
        pass
    else:
        projects = Mobile.objects.all()
    return render(request, './app/projects.html', {'projects': projects})
