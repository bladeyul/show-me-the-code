import re
import os

def gatherMostImportantWords(path):
	m_words={}
	for logName in os.listdir(path):
		log_path=os.path.join(path,logName)
		words=gatherWords(log_path)
		m_words[log_path]=words

def isWord(word):
	if re.findall("[a-zA-Z]+",word):
		return True
	return False

def gatherWords(log_file):
	words_rate={}
	with open(log_file) as fo:
		data=fo.read()
	words=data.split("\b")
	for word in words:
		if isWord(word):
			if word not in words_rate.keys():
				words_rate[word]=1
			else:
				words_rate[word]+=1
	return most_rate(words_rate,10)

def most_rate(words_rate,count):
	words=[]
	for i in range(count):
		now=0
		now_key=None
		for key,value in words_rate.items():
			if value>now:
				now=value
				now_key=key
		words.append(now_key)
		del words_rate[now_key]
	return words
