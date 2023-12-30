import speech_recognition as sr 
import pyttsx3 as tts 
from apilib import *

r=sr.Recognizer()


while 1:

	try:

		with sr.Microphone() as mic:
			r.adjust_for_ambient_noise(mic,duration=0.2)

			print('listening...')
			audio=r.listen(mic)

			text=r.recognize_google(audio).lower()
			print(f'User: {text}')
			speak=tts.init()

			answer=ApiGpt.ask(text)
			print(f'Ai : {answer}')
			speak.say(answer)
			speak.runAndWait()

	except:
		r=sr.Recognizer()
		continue