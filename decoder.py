import base64

enced=input('Enter encoded string : ')

try:
	enced=enced.encode()
	print(base64.b64decode(enced).decode())
except:
	print(base64.b64decode(enced).decode())
