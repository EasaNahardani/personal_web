# Generated by Django 3.2.12 on 2022-02-19 21:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0009_auto_20220219_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=250, unique=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('language', models.CharField(max_length=250)),
                ('technologies', models.TextField()),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Mobile',
        ),
        migrations.DeleteModel(
            name='Web',
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='library',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('Article', 'Application', 'Library')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
