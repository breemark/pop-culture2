from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from django.utils.translation import ugettext_lazy


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('role', 'country',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'


class UserBioForm(forms.ModelForm):
    active = forms.BooleanField(label= ugettext_lazy('Are you currently searching for jobs?'), widget=forms.CheckboxInput(attrs={'class':'actively-searching p-5',}))
    
    class Meta:
        model = UserProfile
        fields = ('avatar', 'description','wechat','phone','country', 'active', )

    def __init__(self, *args, **kwargs):
        super(UserBioForm, self).__init__(*args, **kwargs)

        self.fields['avatar'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['wechat'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control pb-5'


