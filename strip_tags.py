# From Turkle, "The Programming Historian"
# This routine could be repurposed for a lot of things; but in this case it strips the XML without having to use Beautiful Soup.


def stripTags(html): 
	inside = 0
		# This is sort of a 'switch': "How will we keep track of whether or not we're inside a tag? We can use a number variable called inside which will be 1 (true) if we're inside a tag and 0 (false) if we're not."
	text = ''
	for char in html:
		if char == '<': 
			inside = 1
			continue
			# "The Python continue statement tells the interpreter to jump back to the top of the enclosing loop. So if the character is a left angle bracket, once you've made a note that you're inside a tag, you're finished processing that character."
		elif (inside == 1 and char == '>'):
			inside = 0
			continue
		elif inside == 1:
			continue 
		else:
			text += char 
	return text