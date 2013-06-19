from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from apps.core.views import viewbox

urlpatterns = patterns('',
    url(r'^$', '{{ project_name }}.views.viewbox'),
    url(r'^admin/', include(admin.site.urls)),
)
