import os
import random
import speech_recognition as sr
from fuzzysearch import find_near_matches

AUDIO_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                          'navigation/static/navigation/audiofiles')

commands = ['sensory_counting', 'mantra', 'object', 'breathing']


def prompt_user():
    return os.path.join(AUDIO_PATH, 'prompt.mp3')

def launch_exercise():
    user_in = accept_audio()
    command = process_speech(user_in)
    path = exercise_path(command)
    return path


# reads audio from mic
def accept_audio():
    mic = sr.Microphone()
    rec = sr. Recognizer()

    try:
        with mic as source:
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
        return rec.recognize_google(audio)
    except sr.UnknownValueError:
        return ''


# reads audio from file
def speech_to_text(audio_input):
    rec = sr.Recognizer()  # Speech Recognizer

    af = sr.AudioFile(audio_input) # Audio File
    try:
        with af as source:
            audio = rec.record(source) # Audio Data
            return rec.recognize_google(audio)
    except sr.UnknownValueError:
        return ''


def process_speech(transcript):
    if find_near_matches('count', transcript, max_l_dist=2) or find_near_matches('sens', transcript, max_l_dist=2):
        return 'sensory_count'
    if find_near_matches('mantra', transcript, max_l_dist=2) or find_near_matches('make', transcript, max_l_dist=2):
        return 'mantra'
    if find_near_matches('breath', transcript, max_l_dist=2):
        return 'breathing'
    if find_near_matches('focus', transcript, max_l_dist=2) or find_near_matches('object', transcript, max_l_dist=2):
        return 'object'
    return ''


def exercise_path(command):
    if command == '': # random exercise
        index = random.randint(0, len(commands)-1)
        command = commands[index]
    return os.path.join(AUDIO_PATH, command +'.mp3')
