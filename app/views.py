from django.shortcuts import render
from .models import Skill




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
