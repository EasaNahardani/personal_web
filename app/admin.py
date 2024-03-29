from django.contrib import admin
from django.utils.translation import activate
from parler.admin import TranslatableAdmin
from .models import Skill, ContactMessage, Library, Article, Application, Image
from .forms import ArticleForm, ApplicationForm, LibraryForm
#from django.contrib.contenttypes.models import ContentType

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('name', 'level')
    search_fields = ('name',)



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sender_mail', 'sender_phone', 'sent_at')
    list_filter = ('sent_at', )
    search_fields = ('full_name', 'sender_mail', 'sender_phone')



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'project', 'image_tag')
    # list_filter = ('project', )            # this raise an error : 'GenericForeignKey' object has no attribute 'choices'



class ProjectAdmin(TranslatableAdmin):
    list_display = ['title', 'status', 'url']
    list_filter = ['created',]
    search_fields = ['title',]
    #prepopulated_fields = {'slug': ('title',)}
    add_form_template = 'parler/change_form.html'
    change_form_template = 'parler/change_form.html'

    #def get_prepopulated_fields(self, request, obj=None):
    #    return {'slug': ('title',)}

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['form'] = self.get_form(request)
        return super().add_view(request, form_url=form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        obj.save()
        images = request.FILES.getlist('images_list')
        for img in images:
            # Image.objects.create(project=obj, image=img)       # solution 2
            obj.images.create(image=img)
        return super().save_model(request, obj, form, change)



@admin.register(Article)
class ArticleAdmin(ProjectAdmin):
    def get_form(self, request, obj=None, **kwargs):
        try:
            instance = kwargs['instance']
            return ArticleForm(instance=instance)
        except KeyError:
            return ArticleForm

    def change_view(self, request, object_id, form_url="", extra_context=None):
        lang = request.GET.get('language', 'en')
        extra_context = extra_context or {}
        article = Article.objects.language(lang).get(id=object_id)
        extra_context["form"] = self.get_form(request, instance=article)
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)




@admin.register(Application)
class ApplicationAdmin(ProjectAdmin):
    def get_form(self, request, obj=None, **kwargs):
        try:
            instance = kwargs['instance']
            return ApplicationForm(instance=instance)
        except KeyError:
            return ApplicationForm

    def change_view(self, request, object_id, form_url="", extra_context=None):
        lang = request.GET.get('language', 'en')
        extra_context = extra_context or {}
        app = Application.objects.language(lang).get(id=object_id)
        extra_context["form"] = self.get_form(request, instance=app)

        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)




@admin.register(Library)
class LibraryAdmin(ProjectAdmin):
    def get_form(self, request, obj=None, **kwargs):
        try:
            instance = kwargs['instance']
            return LibraryForm(instance=instance)
        except KeyError:
            return LibraryForm

    def change_view(self, request, object_id, form_url="", extra_context=None):
        lang = request.GET.get('language', 'en')
        extra_context = extra_context or {}
        library = Library.objects.language(lang).get(id=object_id)
        extra_context["form"] = self.get_form(request, instance=library)
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)
