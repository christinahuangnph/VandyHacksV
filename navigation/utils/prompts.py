import os
import random
import speech_recognition as sr
from fuzzysearch import find_near_matches

AUDIO_PATH = '/static/navigation/audiofiles'

commands = ['mantra', 'object', 'breathing']


def prompt_user():
    return AUDIO_PATH + '/prompt.mp3'

def launch_exercise():
    user_in = accept_audio()
    command = process_speech(user_in)
    path = exercise_path(command)
    return (path, command)


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
        return 'unknown value'


def process_speech(transcript):
    if find_near_matches('mantra', transcript, max_l_dist=2):
        return 'mantra'
    if find_near_matches('breath', transcript, max_l_dist=2):
        return 'breathing'
    if find_near_matches('focus', transcript, max_l_dist=2):
        return 'object'
    # pick random command
    print("we're going random")
    index = random.randint(0, len(commands) - 1)
    return commands[index]


def exercise_path(command):
    return AUDIO_PATH + '/' + command + '.mp3'

