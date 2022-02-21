from django.shortcuts import render, redirect
from .models import Skill, Application, Article, Library, ContactMessage
from .forms import ContactMessageForm


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def home(request):
    return render(request, './app/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    else:
        form = ContactMessageForm()
    return render(request, './app/contact.html', {'form':form})


def about(request):
    return render(request, './app/about.html')


def education(request):
    return render(request, './app/education.html')


def skills(request):
    skills = Skill.objects.all()
    return render(request, './app/skills.html', {'skills':skills})


def projects(request):
    category = request.GET.get('category', None)
    if category:
        if category == 'article':
            projects = Article.objects.all() #prefetch_related('images')
        else:
            projects = Library.objects.all() #prefetch_related('images')
    else:
        projects = Application.objects.all() #prefetch_related('images')
    return render(request, './app/projects.html', {'projects': projects})
