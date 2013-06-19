from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from apps.core.views import viewbox

urlpatterns = patterns('',
    url(regex=r'^$', view=viewbox, name="viewbox"),
    url(regex=r'^admin/', view=include(admin.site.urls), name="admin"),
)
