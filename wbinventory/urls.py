from django.conf.urls.defaults import patterns, url
from django.views.generic.edit import UpdateView, CreateView
from wbinventory.forms import ItemForm
from wbinventory.models import Item, ItemTransaction
from wbinventory.views import SiteSearchListView, ItemDetailView, ItemTransactionCreateView


urlpatterns = patterns('wbinventory.views',
    url(
        r'^$',
        'index',
        name='wbinventory_index',
    ),
    url(
        r'^items/create/$',
        CreateView.as_view(
            context_object_name='item',
            template_name='wbinventory/item/create.html',
            model=Item,
            form_class=ItemForm,
        ),
        name='wbinventory_item_create',
    ),
    url(
        r'^items/(?P<pk>\d+)/$',
        ItemDetailView.as_view(
            context_object_name='item',
            template_name='wbinventory/item/detail.html',
            model=Item,
        ),
        name='wbinventory_item_detail',
    ),
    url(
        r'^items/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            context_object_name='item',
            template_name='wbinventory/item/update.html',
            model=Item,
            form_class=ItemForm,
        ),
        name='wbinventory_item_update',
    ),
    url(
        r'^itemtransactions/create/$',
        ItemTransactionCreateView.as_view(
            context_object_name='itemtransaction',
            model=ItemTransaction,
        ),
        name='wbinventory_itemtransaction_create',
    ),
    url(
        r'^search/$',
        SiteSearchListView.as_view(),
        name='wbinventory_sitesearch',
    ),
)
