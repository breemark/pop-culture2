from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Menu, Post
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    # Get Language Code
    # If Chinese, send Chinese, otherwise send English 
    # Also send the latest jobs, according to the langauge
    if request.LANGUAGE_CODE == 'en-us':
        mainpage = Menu.objects.get(slug='main')
        jobs = Post.objects.all().filter(language='en-us', active=True,).order_by('-id')[:7]

    elif request.LANGUAGE_CODE == 'zh-hans':
        mainpage = Menu.objects.get(slug='main-chinese')
        jobs = Post.objects.all().filter(language='zh-hans', active=True,).order_by('-id')[:7]

    return render(request, 'cms/home.html', {'mainpage':mainpage, 'jobs': jobs})


def menu_content(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    if menu != 'admin/' or menu != 'posts':
        return render(request, 'cms/page.html', {'menu': menu})


def job_content(request, job_slug):
    job = get_object_or_404(Post, slug=job_slug)
    return render(request, 'jobs/post.html', {'job': job})


def job_listing(request):
    job_list = Post.objects.get_queryset().order_by('id')
    paginator = Paginator(job_list, 10) # Show 10 jobs per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jobs/list.html', {'page_obj': page_obj})