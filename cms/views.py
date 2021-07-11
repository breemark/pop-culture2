from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings


# Create your views here.
def home(request):
    # Get Language Code
    # If Chinese, send Chinese, otherwise send English 
    return render(request, 'cms/home.html', {})

