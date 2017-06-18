# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 14:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(height_field='height_field', upload_to=posts.models.upload_location, width_field='width_field')),
                ('description', models.CharField(default='', max_length=512)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='user_like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
