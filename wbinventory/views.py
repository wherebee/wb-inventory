import re
from django.core.exceptions import PermissionDenied
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.list import ListView
from wbinventory.forms import ItemForm
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

    @property
    def normalized_q(self):
        q = self.request.GET['q']
        q = re.sub(r'\s{2,}', ' ', q.strip()) # Normalize whitespace.
        return q

    def get_context_data(self, **kwargs):
        data = super(SiteSearchListView, self).get_context_data(**kwargs)
        # Do we have an exact item number match?
        if not len(self.get_queryset_exact_match()):
            data['create_item_form'] = ItemForm(dict(
                number=self.normalized_q,
            ))
        data['has_exact_match'] = 0 < len(self.get_queryset_exact_match())
        return data

    def get_queryset_exact_match(self):
        q = self.normalized_q
        if q:
            return Item.objects.filter(number__iexact=q)
        else:
            return None

    def get_queryset(self):
        q = self.normalized_q
        if q:
            return Item.objects.filter(
                Q(number__icontains=q) | Q(name__icontains=q),
            )
        else:
            return None
