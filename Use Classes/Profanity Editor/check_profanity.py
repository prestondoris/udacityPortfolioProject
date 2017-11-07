import urllib

def read_text():
	quotes = open("/Users/prestonc.doris/Desktop/Web Development/Udacity/Full Stack Web Dev Nano/Use Classes/Profanity Editor/movie_quotes.txt")
	contents = quotes.read()
	print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(text_to_check):
	#urlopen() works just like the open() function except you
	#supply a url instead of the local file path
	connection  = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	print output
	connection.close()

read_text()