import media
import fresh_tomatoes

#import media is telling your program that you want to use 
#the contents of your python module(file) called media
#good practice states that you should keep your class 
#definitions in one file and use/call the class in another file.

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life.",
						"http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", 
					 "A marine on an alien planet",
					 "http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
boondock_saints = media.Movie("The Boondock Saints",
							  "Two brothers impose vigilanty justice based on a premonetion from God",
							  "http://imgc.allpostersimages.com/img/posters/boondock-saints-shepherd-movie-poster_u-L-F7P1DK0.jpg",
							  "https://www.youtube.com/watch?v=VoRrQiORYck")
braveheart = media.Movie("Braveheart",
						 "A Scottish hero frees his country from English rule",
						 "https://images-na.ssl-images-amazon.com/images/I/A1vggsn4DjL._SY550_.jpg",
						 "https://www.youtube.com/watch?v=1cnoM8EiGGU")
pitch_perfect = media.Movie("Pitch Perfect",
							"An all womens College acapella group takes on their male counter parts",
							"https://globalincentivesinc.files.wordpress.com/2015/10/pitch-perfect-movie-poster-21.jpg",
							"https://www.youtube.com/watch?v=8dItOM6eYXY")
snatch = media.Movie("Snatch",
					 "Illegal boxing promoter convinces a gangster to offer bets on bare-knuckle boxer Mickey at his bookie business.",
					 "https://fluffpot.files.wordpress.com/2014/04/snatch.jpg",
					 "https://www.youtube.com/watch?v=ni4tEtuTccc")


movies = [toy_story, avatar, boondock_saints, braveheart, pitch_perfect, snatch]
fresh_tomatoes.open_movies_page(movies)
