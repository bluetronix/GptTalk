from apilib import *

while 1:
	q=input('Ask anything: ')
	print(ApiGpt.ask(q))