from django.http import HttpResponseRedirect, HttpR

from .utils import prompts


def index(request):
    if(request.method == 'POST'): # form submission
        return 0
