# Import the libraries
import speech_recognition as sr
import warnings
import random
from playsound import playsound

warnings.filterwarnings('ignore')


# Record audio and return it as a string
def recordAudio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Speak')
        audio = r.listen(source)

    # Speech recognition using Google's Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('...')

    except sr.RequestError as e:
        print('Request error from Google Speech Recognition')
    return data


# Function to get the virtual assistant response MAKES/SAVES/PLAYS RESPONSE
def assistantResponse(text):
    print(text)  # Convert the text to speech


# A function to check for wake word(s) RETURNS TRUE/FALSE
def wakeWord(text):
    WAKE_WORDS = ['alpha']
    text = text.lower()  # Convert the text to all lower case words
    # Check to see if the users command/text contains a wake word
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True  # If the wake word was not found return false
    return False


# Function to return a random greeting response
def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']
    # Greeting Response back to the user
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
    # If the users input is a greeting, then return random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'  # If no greeting was detected then return an empty string
    return ''


quitstate: bool = True

while quitstate:
    # Record the audio

    text = recordAudio()
    response = ''  # Empty response string

    # Checking for the wake word/phrase
    if wakeWord(text):
        playsound('R2D2.mp3')
        # Check for greetings by the user
        response = response + greeting(text)

        if 'grab' in text:
            # grabObjected = grabOBJ()
            response = response + 'on it!'  # Check to see if the user said time
        if 'quit' in text:
            # grabObjected = grabOBJ()
            quitstate = False

    # Assistant Audio Response
    assistantResponse(response)
