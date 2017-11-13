import webbrowser


class Movie():
    """
    The class Movie provides a way to store the Title, brief
    story line information, a link to a movie poster image,
    and a link to the movie trailer on youtube.
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
