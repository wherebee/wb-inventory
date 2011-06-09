from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


def index(request):
    if not request.user.has_module_perms('wbinventory'):
        raise PermissionDenied()
    return HttpResponse('')
