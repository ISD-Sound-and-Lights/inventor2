#!/usr/local/bin/python3
import os.path
from sys import path as syspath
syspath.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from assets import *

print("Content-Type: text/html;charset=utf-8\n")
cgitb.enable()


ErrorTemplate = Template('error', errorNumber=500, loginPretty='logged in as: root')
print(str(ErrorTemplate))
