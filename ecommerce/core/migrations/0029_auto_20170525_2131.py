# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-26 01:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_siteconfiguration_optimizely_snippet_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='theme_scss_path',
            field=models.CharField(blank=True, help_text=b'DEPRECATED: THIS FIELD WILL BE REMOVED!', max_length=255,
                                   null=True, verbose_name='Path to custom site theme'),
        ),
    ]
