# Generated by Django 3.2.12 on 2022-02-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220224_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='technologies',
            field=models.TextField(default='git'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='technologies',
            field=models.TextField(default='git'),
            preserve_default=False,
        ),
    ]
