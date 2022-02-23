from parler.models import  TranslatedFields
from app import models
# import inspect    # to inspect attributes and functions available in a class

class AllTranslatedFields(TranslatedFields):

    def __init__(self,  meta=None, **fields):
        #all_fields = self.model._meta.get_fields() # raise an error that has not model
        #for field in all_fields:
        #    if field.attname == '':

        #if hasattr(models.Project, 'abstract_translations'):
        #models.Project.__dict__.keys()  # get all class attributes

        #members = inspect.getmembers(models.Project, lambda a:not(inspect.isroutine(a)))
        #print([a for a in members if not(a[0].startswith('__') and a[0].endswith('__'))])  # get all class attributes except buit-in

        #print('abstract_translations' in dir(models.Project) )
        #print(models.Project.__dict__.items())

        #fields.update(models.Project.abstract_translations)
        super().__init__(meta, **fields)


    def contribute_to_class(self, cls, name, **kwargs):
        # Called from django.db.models.base.ModelBase.__new__
        super().contribute_to_class(cls, name, **kwargs)
