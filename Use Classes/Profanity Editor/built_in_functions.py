def read_text():
	quotes = open("/Users/prestonc.doris/Desktop/Web Development/Udacity/Full Stack Web Dev Nano/Use Classes/Profanity Editor/numbers.txt")
	contents = quotes.read()
	contentsList = contents.split()
	numberList = [int(i) for i in contentsList]
	product = 1
	i = 0
	while i < len(numberList):
		print numberList[i]
	 	product = product*numberList[i]
	 	i += 1
	
	print "The product of the list of numbers above is:"
	print product

	quotes.close()

read_text()