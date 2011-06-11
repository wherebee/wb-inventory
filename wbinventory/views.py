from django.core.exceptions import PermissionDenied
from django.shortcuts import render


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


@require_any_perm
def sitesearch(request):
    return render(request, 'wbinventory/sitesearch.html', {})
