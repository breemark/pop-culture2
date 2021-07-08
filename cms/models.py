from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from unidecode import unidecode



LANGUAGE_CODE = (
    ('en-us', 'English'),
    ('zh-cn', 'Simplified Chinese'),
)

class Menu(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextField(blank=True, null=True)
    language = models.CharField(max_length=5, choices=LANGUAGE_CODE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title)


class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextField(blank=True, null=True)
    language = models.CharField(max_length=5, choices=LANGUAGE_CODE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title)
