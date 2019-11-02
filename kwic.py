# Key Word In Context Routine
# based on Turkle text


def prettyPrintKWIC(kwic): 
	n = len(kwic)
	keyindex = n // 2
	width = 7
	outstring = ' '.join(kwic[:keyindex]).rjust(width*keyindex) 
	outstring += str(kwic[keyindex]).center(len(kwic[keyindex])+9) 
	outstring += ' '.join(kwic[(keyindex+1):])
	return outstring



# __String Formatting__ 

	# Extra spacing:

		#"We want the keywords to have a bit of whitespace padding around them. We can achieve this by using a string method called center and having the overall string be longer than the keyword itself. The expression below adds three blank spaces (6/2) to either side of the keyword. We've added hash marks at the beginning and end of the expression so you can see the leading and trailing blanks:"

		#print '#' + str(kwic[keyindex]).center(len(kwic[keyindex])+6) + '#' 
		#-> # iroquois #

	# Justifying:

		#"Finally, we want the left-hand context to be right justified. Depending on how large n is, we are going to need the overall length of this column to increase. We do this by defining a variable called width and then making the column length a multiple of this variable (we used a width of 10 characters, but you can make it larger or smaller as desired). The rjust method handles right justification. Once again, we've added hash marks so you can see the leading blanks:"

		#width = 10
		#print '#' + ' '.join(kwic[:keyindex]).rjust(width*keyindex) + '#'
		#-> #                 killed by the#




