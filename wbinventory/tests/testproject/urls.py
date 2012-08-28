from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    # mount wbinventory app
    url(
        r'^wbinventory/',
        include('wbinventory.urls'),
    ),

    # authentication
    url(
        r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='accounts_login',
    ),
    url(
        r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='accounts_logout',
    ),
)
