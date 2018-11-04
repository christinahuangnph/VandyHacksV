from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .utils import prompts
from .utils import upload

@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')


def audio(request):
    if (request.method == 'POST'):  # form submission
            return upload.handle_uploaded_file(request.FILES['file'])
