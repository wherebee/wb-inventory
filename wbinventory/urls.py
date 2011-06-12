from django.conf.urls.defaults import patterns, url
from django.views.generic.detail import DetailView
from wbinventory.models import Item
from wbinventory.views import SiteSearchListView


urlpatterns = patterns('wbinventory.views',
    url(
        r'^$',
        'index',
        name='wbinventory_index',
    ),
    url(
        r'^items/(?P<pk>\d+)/$',
        DetailView.as_view(
            context_object_name='item',
            template_name='wbinventory/item/detail.html',
            model=Item,
        ),
        name='wbinventory_item_detail',
    ),
    url(
        r'^search/$',
        SiteSearchListView.as_view(),
        name='wbinventory_sitesearch',
    ),
)
