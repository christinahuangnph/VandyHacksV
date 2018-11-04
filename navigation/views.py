from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .utils import prompts

@ensure_csrf_cookie
def index(request):

    if(request.method == 'POST'): # form submission
        return JsonResponse({'prompt':prompts.prompt_user(),
                             'exercise': prompts.launch_exercise()})

    return render(request, 'index.html')
