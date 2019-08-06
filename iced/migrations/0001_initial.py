# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-30 18:51
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KonnectProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county', models.CharField(default='Kajiado', max_length=50)),
                ('specialisation', models.CharField(default='Livestock', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='image.png', upload_to='profiles/')),
                ('name', models.CharField(max_length=30)),
                ('bio', tinymce.models.HTMLField(default='About me', max_length=500)),
                ('task', models.IntegerField()),
                ('county', models.CharField(default='Kajiado', max_length=50)),
                ('specialisation', models.CharField(default='Livestock', max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('average_vote', models.FloatField(default=0)),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iced.Profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
