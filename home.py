from flask import Flask
from flask import url_for

name = ""
city_names = ["city_1", "city_2"]

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
	code ="""
	<head>
	</head>
	<body>
		<h1>Welcome """ + name + """ !</h1>
		<a href= "https://www.google.com/"> not google </a>
		<ul>
	"""
	for city in city_names:
		code = code + "<li>" + city + "<li>"
		code = code + """</ul> </body>"""
	return code

@myapp_obj.route("/hello")
def hello():
	user = {"useranme" : "bao"}
	return '''
	<html>
	<head>
		<title> Home Page - my blog</title>
	</head>
	<body>
		<h1>Hello, ''' + user["username"] + '''!</h1>
	</body>
	</html>'''

myapp_obj.run()
