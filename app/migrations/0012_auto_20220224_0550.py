# Generated by Django 3.2.12 on 2022-02-24 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_translations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='applicationtranslation',
            name='technologies',
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='library',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='librarytranslation',
            name='technologies',
        ),
    ]