import media

#import media is telling your program that you want to use 
#the contents of your python module(file) called media

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life.",
						"http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar", 
					 "A marine on an alien planet",
					 "http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg",
					 "https://www.youtube.com/watch?v=a0CDJZu4M5I")

print(avatar.storyline)

boondock_saints = media.Movie("The Boondock Saints",
							  "Two brothers impose vigilanty justice based on a premonetion from God",
							  "http://imgc.allpostersimages.com/img/posters/boondock-saints-shepherd-movie-poster_u-L-F7P1DK0.jpg",
							  "https://www.youtube.com/watch?v=VoRrQiORYck")

boondock_saints.show_trailer()


#good practice states that you should keep your class 
#definitions in one file and use/call the class in another file.