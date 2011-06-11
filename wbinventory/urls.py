from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('wbinventory.views',
    url(regex=  r'^$',
        name=   'wbinventory_index',
        view=   'index',
    ),
    url(
        regex=  r'^search/$',
        name=   'wbinventory_sitesearch',
        view=   'sitesearch',
    ),
)
