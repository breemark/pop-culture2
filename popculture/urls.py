import cms
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('cms.urls')),
    path('', include('videos.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    prefix_default_language=True
)     


     
# urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Pop Culture"
admin.site.site_title = "Pop Culture Shenzhen"
admin.site.index_title = "Welcome to Pop Culture System"