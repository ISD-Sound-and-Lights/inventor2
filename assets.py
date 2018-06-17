import os
import os.path
import cgi
import cgitb
import bcrypt
from http import cookies as Cookie


auth_info = {
		'basic': (b'$2b$12$c66G90rtLuaiNPjaKL4vnupurXCVLq8nSRDn82RFZt0y1aBZrRj0.', b'$2b$12$c66G90rtLuaiNPjaKL4vnu'),
		'standard': (b'$2b$12$8emOe.SX.wgaGeOnUAjIgei/e5B0mIVJrS11J5YZIuVQhiFD./xqy', b'$2b$12$8emOe.SX.wgaGeOnUAjIge'),
		'admin': (b'$2b$12$RUchRgKH36lPdlr7nX5cxe7g5jziRugZ0KUdVNHlLI8YdezU7DSPa', b'$2b$12$RUchRgKH36lPdlr7nX5cxe')
		}


class Template:
	def __init__(self, name, **kwargs):
		templateDirectory = os.path.dirname(os.path.abspath(__file__))  # /path/to/hosting/folder/error
		templateDirectory = templateDirectory.lstrip("error") if templateDirectory.startswith(
			"error") else templateDirectory  # /path/to/hosting/folder
		with open(os.path.join(templateDirectory, "templates",
							   name + ".html")) as templateFile:  # /path/to/hosting/folder/templates/error.html
			self.template = templateFile.read()

		self.final = self.template.format(**kwargs)
		self.replacers = kwargs

	def __str__(self):
		return self.final

	def __repr__(self):
		return self.template, self.replacers,


def authenticate(username, password, checkCookies=True):
	if checkCookies and __checkLoginCookie(): return 1  # cookies were good, so no need to manually check

	username = str(username)
	password = str(password)

	try:
		correctpw = auth_info[username][0]
		salt = auth_info[username][1]
	except KeyError:  # we do the rest anyway to prevent guessing correct usernames based on processing time
		correctpw = b'incorrect username...'
		salt = bcrypt.gensalt()
	hashedpw = bcrypt.hashpw(password.encode(), salt)

	if correctpw == hashedpw:
		return 2
	else:
		return 0


def __checkLoginCookie():
	if "HTTP_COOKIE" in os.environ:
		cookieString = os.environ.get("HTTP_COOKIE")
		cookie = Cookie.SimpleCookie()
		cookie.load(cookieString)

		username = cookie['username'].value
		password = cookie['password'].value

		return authenticate(username, password, checkCookies=False)
	else:
		return False
