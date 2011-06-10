from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response


def index(request):
    if not request.user.has_module_perms('wbinventory'):
        raise PermissionDenied()
    return render_to_response('wbinventory/index.html', {})
