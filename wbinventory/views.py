from django.core.exceptions import PermissionDenied
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from wbinventory.models import Item


def require_any_perm(fn):
    def view(request, *args, **kw):
        if not request.user.has_module_perms('wbinventory'):
            raise PermissionDenied()
        else:
            return fn(request, *args, **kw)
    view.__name__ = fn.__name__
    return view


@require_any_perm
def index(request):
    return render(request, 'wbinventory/index.html', {})


class SiteSearchListView(ListView):

    context_object_name = 'item_list'
    template_name = 'wbinventory/sitesearch.html'

    def get_queryset(self):
        q = self.request.GET['q']
        if q:
            return Item.objects.filter(
                Q(number__icontains=q) | Q(name__icontains=q),
            )
        else:
            return None
