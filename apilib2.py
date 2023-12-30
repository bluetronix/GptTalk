import os
from openai import OpenAI
#upon execution rename this script to apilib or just adjust the importation of the other scripts

class ApiGpt:

	def ask(msg):
			
		client = OpenAI(
		    # the api key is base 64 encoded ..just decode it and walaah
		    api_key='b'c2stYU5Zd200aDFKTWlsNklrQXRNdVRUM0JsYmtGSlFMOGN5dWMzbVk3clQyZThBaDBN'',
		)

		chat_completion = client.chat.completions.create(
		    messages=[
		        {
		            "role": "user",
		            "content": msg,
		        }
		    ],
		    model="gpt-3.5-turbo",
		)

		return chat_completion.choices[0].message.content