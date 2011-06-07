from django.conf.urls.defaults import *

from djangorestframework.resources import ModelResource
from djangorestframework.views import InstanceModelView, ListOrCreateModelView

from wbinventory.models import Item


class ItemResource(ModelResource):

    model = Item


urlpatterns = patterns('wbinventory.views',
    url(regex=  r'^$',
        name=   'wbinventory_index',
        view=   'index',
    ),
    url(regex=  r'^api/v1/item/$',
        view=   ListOrCreateModelView.as_view(resource=ItemResource),
    ),
    url(regex=  r'^api/v1/item/(?P<pk>[^/]+)/$',
        view=   InstanceModelView.as_view(resource=ItemResource),
    ),
)
