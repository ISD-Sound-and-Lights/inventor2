#!/usr/local/bin/python3
from assets import *

print("Content-Type: text/html;charset=utf-8\n")
cgitb.enable()


ErrorTemplate = Template('index', loginPretty='logged in as: root')
print(str(ErrorTemplate))
