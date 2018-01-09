import media
import fresh_tomatoes

# create a new movie Thor
thor = media.Movie("Thor Ragnarok",
                   "https://goo.gl/QEfn5B",
                   "https://www.youtube.com/watch?v=v8RgYZAAIzY")

# create a new movie avatar
avatar = media.Movie("Avatar",
                     "https://goo.gl/Ys33Jp",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# create a new movie spider-man
spider_man = media.Movie("Spider-Man",
                         "https://i.redd.it/26x9bcgkfezy.jpg",
                         "https://www.youtube.com/watch?v=U0D3AOldjMU")

# create a new movie despicable me
despicable_me = media.Movie("Despicable Me 3",
                            "https://goo.gl/Gu7ExR",
                            "https://www.youtube.com/watch?v=6DBi41reeF0")

# create a new movie matrix
matrix = media.Movie("Matrix",
                     "https://goo.gl/qDQ5bw",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# create a new moive dunkirk
dunkirk = media.Movie("Dunkirk",
                      "https://goo.gl/qV5dvz",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

# store the new moives in an array, and pass it to open_movie_pages
movies = [thor, avatar, spider_man, despicable_me, matrix, dunkirk]
# open_moives_page will take in a moive or an array of movies and
# render them on an html page
fresh_tomatoes.open_movies_page(movies)
