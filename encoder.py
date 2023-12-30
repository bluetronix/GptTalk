import base64

plain=input('Enter string to encode here: ').encode()

enced=base64.b64encode(plain)

print(enced)