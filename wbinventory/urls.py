from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(regex=  r'^$',
        name=   'wbinventory_index',
        view=   direct_to_template,
        kwargs= {
            'template': 'wbinventory/index.html',
        },
    ),
)
