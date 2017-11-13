import media
import fresh_tomatoes

# import media will provide class Movie to store all instances of movies
# which will be supplied to the fresh_tomatoes file which generates the HTML

# Angles of Demons movie: Title, storyline, poster img url, youtube trailer URL
angels_demons = media.Movie(
    "Angels and Demons",
    "A Harvard Symbologist discovers the resurgance of an ancient brotherhood "
	"known as the Illuminati.",
    "https://i.pinimg.com/originals/cc/8b/98/cc8b989262a93cbafb8f79e79f636335.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zzjv-GUEDfg")

# Aavatar movie: Title, storyline, poster img url, youtube trailer URL
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Boondock Saints movie: Title, storyline, poster img url, youtube trailer URL
boondock_saints = media.Movie(
    "The Boondock Saints",
    "Two brothers impose vigilanty justice based on a premonetion from God",
    "http://imgc.allpostersimages.com/img/posters/boondock-saints-shepherd-movie-poster_u-L-F7P1DK0.jpg",  # NOQA
    "https://www.youtube.com/watch?v=VoRrQiORYck")

# Braveheart movie: Title, storyline, poster img url, youtube trailer URL
braveheart = media.Movie(
    "Braveheart",
    "A Scottish hero frees his country from English rule",
    "https://images-na.ssl-images-amazon.com/images/I/A1vggsn4DjL._SY550_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1cnoM8EiGGU")

# Pitch Perfect movie: Title, storyline, poster img url, youtube trailer URL
pitch_perfect = media.Movie(
    "Pitch Perfect",
    "An all womens College acapella group takes on their male counter parts",
    "https://globalincentivesinc.files.wordpress.com/2015/10/pitch-perfect-movie-poster-21.jpg",  # NOQA
    "https://www.youtube.com/watch?v=8dItOM6eYXY")

# Snatch movie: Title, storyline, poster img url, youtube trailer URL
snatch = media.Movie(
    "Snatch",
    "Illegal boxing promoter convinces a gangster to offer bets on "
    "bare-knuckle boxer Mickey at his bookie business.",
    "https://fluffpot.files.wordpress.com/2014/04/snatch.jpg",
    "https://www.youtube.com/watch?v=ni4tEtuTccc")

# Batman Begins movie: Title, storyline, poster img url, youtube trailer URL
batman_begins = media.Movie(
    "Batman Begins",
    "The story of how Bruce Wayne becomes Batman",
    "https://images-na.ssl-images-amazon.com/images/I/41W4a4oxfDL.jpg",
    "https://www.youtube.com/watch?v=QhPqez3CwiM")

# Avengers movie: Title, storyline, poster img url, youtube trailer URL
avengers = media.Movie(
    "Avengers",
    "A collection of super heros comes together to save the world from Alien "
    "invaders.",
    "https://vignette.wikia.nocookie.net/marvelheroes/images/9/98/Avengers-movie-poster-1.jpg/revision/latest?cb=20170713041606",  # NOQA
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Harry Potter Price movie: Title, storyline, poster img url,
# youtube trailer URL
harry_potter_prince = media.Movie(
    "Harry Potter and the Half Blood Prince",
    "The 6th installment of the Harry Potter series, Harry learns the past "
    "of Voldermort from Dumbledor.",
    "https://i.pinimg.com/originals/70/a5/bc/70a5bcfdcb2ddbb981167a1693342176.jpg",  # NOQA
    "https://www.youtube.com/watch?v=jpCPvHJ6p90")

# Create list of all movie instances. This will be supplied to
# fresh_tomatoes.py to generate the movies in the HTML
movies = [angels_demons, avatar, boondock_saints, braveheart, pitch_perfect,
          snatch, batman_begins, avengers, harry_potter_prince]

# Supply our movie list to fresh_tomatoes.py to generate the list of moives
# in our HTML document.
fresh_tomatoes.open_movies_page(movies)
