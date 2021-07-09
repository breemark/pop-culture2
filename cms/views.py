from django.shortcuts import render

# Create your views here.
def home(request):
    # Get Language Code
    # If Chinese, send Chinese, otherwise send English 
    return render(request, 'cms/home.html', {})