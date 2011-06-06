from django.conf.urls.defaults import *

from tastypie.api import Api

from wbinventory.api import ItemResource


v1_api = Api(api_name='v1')
v1_api.register(ItemResource())


urlpatterns = patterns('wbinventory.views',
    url(regex=  '^$',
        name=   'wbinventory_index',
        view=   'index',
    ),
    url(regex=  '^api/',
        view=   include(v1_api.urls),
    ),
)
