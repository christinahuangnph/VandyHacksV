from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .utils import prompts
from .utils import upload

@ensure_csrf_cookie
def index(request):
    if(request.method == 'POST'): # form submission
        return JsonResponse({'exercise': prompts.launch_exercise()})

    return render(request, 'index.html')


def audio(request):
    if (request.method == 'POST'):  # form submission
        form = upload.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return upload.handle_uploaded_file(request.FILES['file'])
