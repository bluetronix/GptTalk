from flet import *
from apilib import *
import speech_recognition as sr
import pyttsx3 as tts
def main(page:Page):
	global fdata
	nb=AlertDialog(
		title=Text("VERY IMPORTANT"),
		content=Text('''Make sure you are connected to the internet
		when you are using this software '''))
	page.dialog=nb
	nb.open=True
	page.update()
	def record(e):
		fdata=''
		

		r=sr.Recognizer()

		try:
			with sr.Microphone() as mic:
				r.adjust_for_ambient_noise(mic,duration=0.2)
				pbar=ProgressBar(color=green,expand=True)
				text_progress=Text('Recording',color=green)
				sbar.controls.append(text_progress)
				sbar.controls.append(pbar)
				page.update()

				audio=r.listen(mic)
				text0=r.recognize_google(audio)
				

				text=f'Query:\n {text0}'

				fdata+=text

				lv.controls.append(
					Container(content=Text(text)
						,bgcolor=green,border_radius=25
						,padding=30))
				page.update()

				sbar.controls.remove(pbar)
				sbar.controls.remove(text_progress)
				page.update()



				response0=ApiGpt.ask(text0)
				status.value='processing....'
				page.update()

				response=f'Response: \n {response0}'
				fdata+=response

				lv.controls.append(
					Container(
						content=Text(response),
						bgcolor='blue',
						border_radius=25,
						padding=30))
				page.update()
				status.value=''
				page.update()
				speak=tts.init()
				speak.say(response0)
				speak.runAndWait()
		except:
			pass

	#alert dialog to be sure to delete the convo
	def yes_del_conv(e):
		ad0.open=False
		page.update()

		lv.controls.clear()
		page.update()
	def no_del_conv(e):
		ad0.open=False
		page.update()
	ad0=AlertDialog(
		title=Text('Are you sure you want to delete the conversation? '),
		actions=[ElevatedButton('Yes',
			on_click=yes_del_conv),
		ElevatedButton('No',
			on_click=no_del_conv)])

	def clear(e):
		page.dialog=ad0
		ad0.open=True
		page.update()


	#about the project
	about_txt='''
	GptTalk is an opensource project 
	created by the founder of Blixen Company (the wenses media)
	it helps simulate human like conversation with the common Ai Assistant
	ChatGpt
	All CopyRights and Credits to BlixenCompany '''
	about_dialog=AlertDialog(
		title=Text("About GptTalk"),
		content=Text(about_txt))

	def abt_project(e):
		page.dialog=about_dialog
		about_dialog.open=True
		page.update()

	green='#00aa00'
	white='white'

	page.title='Gpt Talk'
	page.theme_mode='Dark'


	page.appbar=AppBar(
		title=Text('GPT Talk v1.0.0'),
		center_title=True,
		bgcolor=green,
		color=white,
		actions=[PopupMenuButton(
			items=[
			PopupMenuItem(
				content=ElevatedButton(
					'Clear Conversation',
					color=white,
					bgcolor=green,
					on_click=clear)),
			
			PopupMenuItem(
				content=ElevatedButton(
					'About App/Project',
					color=white,
					bgcolor=green,
					on_click=abt_project))])])
	lv=ListView(spacing=10,auto_scroll=True)

	spage=Stack([Container(bgcolor='black',
		border_radius=30),lv],expand=True)

	sbar=Row()

	status=Text()


	cbar=Row(
		alignment='center',
		controls=[
		IconButton('mic',
			icon_color='white',
			bgcolor=green,
			on_click=record)])

	page.add(spage,status
		,sbar,cbar)


app(target=main)