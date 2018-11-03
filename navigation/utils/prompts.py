import os
import random
import speech_recognition as sr

AUDIO_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                          'static/navigation/audiofiles')

commands = ['sensory_countingg', 'personal_info']

def prompt_user():
    return os.path.join(AUDIO_PATH, 'promt.mp3')


def process_speech(transcript):
    return 0

def speech_to_text(audio_input):
    rec = sr.Recognizer()  # Speech Recognizer

    af = sr.AudioFile(audio_input) # Audio File
    with af as source:
        audio = rec.record(source) # Audio Data


    return rec.recognize_google(audio)


def launch_exercise(command):
    if command == '': # random exercise
        index = random.randint(len(commands)-1)
        command = commands[index]
    os.path.join(AUDIO_PATH, command +'.mp3')

res = speech_to_text(os.path.join(AUDIO_PATH, 'testing.wav'))
print(res)