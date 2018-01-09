import webbrowser


class Movie():
    """
    This is the contructor for movie, a new movie will be created

    Atributes:
        title(str): the movie's title
        poster_image_url(str): a link to the movie's poster image
        trailer_youtube_url(str): a link to the movie's trailer on Youtube
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
