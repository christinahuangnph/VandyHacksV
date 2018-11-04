import tempfile
import wave

from django.http import JsonResponse
from navigation.utils import prompts


def handle_uploaded_file(f):
    tf = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    for chunk in f.chunks():
        tf.write(chunk)
    tf.close()
    text = prompts.speech_to_text(tf.name)
    print('text: ' + text)
    command = prompts.process_speech(text)
    return JsonResponse({'exercise': [prompts.exercise_path(command), command]})

