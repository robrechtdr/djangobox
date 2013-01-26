from django.conf.urls import patterns, include, url
import {{ project_name }}.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', '{{ project_name }}.views.viewbox'),
    url(r'^admin/', include(admin.site.urls)),
)
