from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from django.templatetags.static import static # is not a template tag
from django.utils import translation
from .models import Skill, Application, Article, Library, ContactMessage
from .forms import ContactMessageForm



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def home(request):
    url = static('img/SORanking.PNG')
    s2 = _('check me  here')
    s1 = _('Recently 400th rank in')
    lang_code = request.LANGUAGE_CODE
    bidi = translation.get_language_info(lang_code)['bidi']
    if not bidi:
        display = 'inline'
        percent = '0.74%'
    else:
        display = 'inline-block'
        percent = '0/74%'
    # from django.contrib.messages import constants
    # or constants.INFO   or  messages.INFO
    messages.add_message(request, messages.INFO ,
                            mark_safe('<svg aria-hidden="true" class="svg-icon iconAchievements"'\
                            ' width="18" height="18" viewBox="0 0 18 18"><path fill="#e0cc0f" d="M15 2V1H3v1H0v4c0 1.6 1.4 3 3 3v1c.4 1.5 3 2.6 5 3v2H5s-1 1.5-1'\
                            ' 2h10c0-.4-1-2-1-2h-3v-2c2-.4 4.6-1.5 5-3V9c1.6-.2 3-1.4 3-3V2h-3ZM3 7c-.5 0-1-.5-1-1V4h1v3Zm8.4 2.5L9 8 6.6 9.4l1-2.7L5'\
                            ' 5h3l1-2.7L10 5h2.8l-2.3 1.8 1 2.7h-.1ZM16'\
                            ' 6c0 .5-.5 1-1 1V4h1v2Z"></path></svg>'\
                            '<span>%(s1)s <span style="font-weight:500;">Stack Overflow</span> '\
                            '<span style="white-space: nowrap;display:%(display)s">(top %(percent)s)</span></span><a href="%(url)s">%(s2)s</a>' % {'s1': s1,
                                                                                                                        'url': url,
                                                                                                                        's2':s2,
                                                                                                                        'display':display,
                                                                                                                        'percent':percent,
                                                                                                                        }),
                                                                                                                        extra_tags='important'
                            )

    return render(request, './app/home.html')



def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Message sent successfully'))
            return redirect('app:home')
        else:
            messages.error(request, _('Error submitting your message'))
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
            objs = Article.objects
            if objs.exists():
                projects = objs.all() #prefetch_related('images')
            else:
                projects = []
                messages.info(request, _('No Articles!'))
        else:
            projects = Library.objects.all() #prefetch_related('images')
    else:
        projects = Application.objects.all() #prefetch_related('images')
    return render(request, './app/projects.html', {'projects': projects})
