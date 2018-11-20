from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings

from donuts import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^donuts/(?P<nameID>\w+)/$', views.site_donutPage, name='DonutPage'),
    url(r'^donuts/$', views.site_allPage, name='AllPage'),
    url(r'^$', views.site_mainPage, name='MainPage'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
