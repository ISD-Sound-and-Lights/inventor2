import os.path
import cgi
import cgitb


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
