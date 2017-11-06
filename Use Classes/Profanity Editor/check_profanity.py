def read_text():
	quotes = open("/Users/prestonc.doris/Desktop/Web Development/Udacity/Full Stack Web Dev Nano/Use Classes/Profanity Editor/movie_quotes.txt")
	contents = quotes.read()
	print(contents)
	quotes.close()

read_text()