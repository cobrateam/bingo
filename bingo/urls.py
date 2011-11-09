from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView
from django.contrib import admin

from post.models import Post

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Post,
                                template_name="index.html"
                               ),
        name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

