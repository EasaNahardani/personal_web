from django.shortcuts import render




def home(request):
    return render(request, './app/home.html')


def contact(request):
    return render(request, './app/contact.html')


def about(request):
    return render(request, './app/about.html')


def education(request):
    return render(request, './app/education.html')
