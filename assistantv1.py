import speech_recognition as sr 
import pyttsx3 as tts 

r=sr.Recognizer()


while 1:

	try:

		with sr.Microphone() as mic:
			r.adjust_for_ambient_noise(mic,duration=0.2)

			print('listening...')
			audio=r.listen(mic)

			text=r.recognize_google(audio).lower()
			speak=tts.init()

			if text=='hello':
				speak.say('hi there')
				speak.runAndWait()
			else:
				speak.say('i dont think I have a response')
				speak.runAndWait()

	except:
		r=sr.Recognizer()
		continue