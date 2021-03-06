# Generated by Django 3.2.5 on 2021-07-08 20:57

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title_format')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('language', models.CharField(choices=[('en-us', 'English'), ('zh-cn', 'Simplified Chinese')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title_format')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('language', models.CharField(choices=[('en-us', 'English'), ('zh-cn', 'Simplified Chinese')], max_length=5)),
            ],
        ),
    ]
