from django.conf import settings
from django.http import HttpResponseRedirect


def index(request):
    # Redirect to the web app's static HTML page.
    url = '{0}wbinventory/wbinventory.html'.format(settings.STATIC_URL)
    return HttpResponseRedirect(url)
