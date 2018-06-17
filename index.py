#!/usr/local/bin/python3
from assets import *
from http import cookies as Cookie

LocalStorage = cgi.FieldStorage()
authenticatedState = authenticate(LocalStorage.getvalue('username'), LocalStorage.getvalue('password'))
if authenticatedState == 1:
	loggedIn = True
elif authenticatedState == 2:
	print('Set-Cookie: username="{}";'.format(LocalStorage.getvalue('username')))
	print('Set-Cookie: password="{}";'.format(LocalStorage.getvalue('password')))
	loggedIn = True
elif authenticatedState == 0:
	loggedIn = False

print("Content-Type: text/html;charset=utf-8\n")
cgitb.enable()

PageTemplate = Template('index', loginPretty='logged in as: root' if loggedIn else 'not logged in')
print(str(PageTemplate))
