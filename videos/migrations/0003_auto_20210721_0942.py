# Generated by Django 3.2.5 on 2021-07-21 01:42

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wechat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
