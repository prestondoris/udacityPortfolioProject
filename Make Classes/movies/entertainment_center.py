import media
import fresh_tomatoes

#import media is telling your program that you want to use 
#the contents of your python module(file) called media
#good practice states that you should keep your class 
#definitions in one file and use/call the class in another file.

angels_demons = media.Movie("Angels and Demons",
						"A Harvard Symbologist discovers the resurgance of an ancient brotherhood know as the Illuminati.",
						"https://i.pinimg.com/originals/cc/8b/98/cc8b989262a93cbafb8f79e79f636335.jpg",
						"https://www.youtube.com/watch?v=zzjv-GUEDfg")
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
batman_begins=media.Movie("Batman Begins",
						  "The story of how Bruce Wayne becomes Batman",
						  "https://images-na.ssl-images-amazon.com/images/I/41W4a4oxfDL.jpg",
						  "https://www.youtube.com/watch?v=QhPqez3CwiM")
avengers=media.Movie("Avengers",
					 "A collection of super heros comes together to save the world from Alien invaders.",
					 "https://vignette.wikia.nocookie.net/marvelheroes/images/9/98/Avengers-movie-poster-1.jpg/revision/latest?cb=20170713041606",
					 "https://www.youtube.com/watch?v=eOrNdBpGMv8")
harry_potter_half_blood_prince=media.Movie("Harry Potter and the Half Blood Prince",
						  					"The 6th installment of the Harry Potter series, Harry learns the past of Voldermort from Dumbledor.",
						  					"https://i.pinimg.com/originals/70/a5/bc/70a5bcfdcb2ddbb981167a1693342176.jpg",
						  					"https://www.youtube.com/watch?v=jpCPvHJ6p90")


movies = [angels_demons, avatar, boondock_saints, braveheart, pitch_perfect, snatch, batman_begins, avengers, harry_potter_half_blood_prince]
fresh_tomatoes.open_movies_page(movies)
