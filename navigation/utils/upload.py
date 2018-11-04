import tempfile
from navigation.utils import prompts
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    with tempfile.TemporaryFile() as tf:
        for chunk in f.chunks():
            tf.write(chunk)
        return prompts.exercise_path(prompts.process_speech(tf.read()))
