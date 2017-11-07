import webbrowser

class Movie():
	#Things to remember
		#title
		#storyline
		#poster_image
		#youtube_trailer
	#Things to do
		#show_trailer()
	

	def __init__(self, movie_title, movie_storyline, 
				 poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster = poster_image
		self.trailer = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer)
