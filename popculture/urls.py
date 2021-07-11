import cms
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _



urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('cms.urls')),
    prefix_default_language=True
)     

