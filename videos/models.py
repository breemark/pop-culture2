from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


# Create your models here.
# TODO
# 2 kinds of profiles, schools and teachers. Teachers can upload video and schools need a special boolean permission to exist
# Both users see their own profile and info when they log in
# Schools have the choice to list through the teachers. Do it with pagination
# User AVATAR
# User VIDEO

USER_ROLES = (
    ('e', 'Employee'),
    ('c', 'Company'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    description = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=1, choices=USER_ROLES)
    authorized = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/') 
    wechat = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(unique = True, null = True, blank = True) # Here
    country = CountryField(blank_label='(select country)')
    video = models.FileField(blank=True, null=True, upload_to='videos/')


    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)