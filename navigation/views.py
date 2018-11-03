from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .utils import prompts

@ensure_csrf_cookie
def index(request):
    context = {}
    if(request.method == 'POST'): # form submission
        context['prompt'] = prompts.prompt_user()
        context['exercise'] = prompts.launch_exercise()


    return render(request, 'index.html', context=context)
