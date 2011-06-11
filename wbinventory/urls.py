from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('wbinventory.views',
    url(
        r'^$',
        'index',
        name='wbinventory_index',
    ),
    url(
        r'^search/$',
        'sitesearch',
        name='wbinventory_sitesearch',
    ),
)
