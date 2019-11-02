# From Turkle, "The Programming Historian"

# Bigger picture: "A program that puts formatting codes around something so that it can be used by another program is called a wrapper."

# Preliminary concept: Python string formatting. "Python includes a special formatting operator that allows you to interpolate one string in another one. It is represented by a percent sign."

# Example:
# frame = 'This is a %s' print frame
# -> This is a %s
# print frame % 'cat'
# -> This is a cat
# print frame % 'dog'
# -> This is a dog


def wrapStringInHTML(program, url, body): 
	import datetime
	from webbrowser import open_new_tab
	now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S") filename = program + '.html'
	f = open(filename,'w')
	wrapper = """<html>
		<head>
		<title>%s output - %s</title>
		</head>
<		body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body> </html>"""
    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()
    open_new_tab(filename)