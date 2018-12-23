import re

def isword(word):
	if re.findall("[a-zA-Z]+",word):
		return True
	return False

def wordCount(fileName):
	count=0
	with open(fileName) as fo:
		data=fo.read()

	doc=data.split("\b")
	for word in doc:
		if isword(word):
			count+=1
	return count





