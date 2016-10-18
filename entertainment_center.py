import media
import fresh_tomatoes

# A list that stores all the movie objects
movie_list = [
    media.movie("Iron Man",
                "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ah.jpg",  # noqa
                "https://www.youtube.com/watch?v=8hYlB38asDY"),
    media.movie("Doctor Strange",
                "http://cdn3-www.superherohype.com/assets/uploads/gallery/doctor-strange/cf5nqhcxiae59i9-jpg-large.jpg",  # noqa
                "https://www.youtube.com/watch?v=HSzx-zryEgM"),
    media.movie("Avengers",
                "http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s",  # noqa
                "https://www.youtube.com/watch?v=eOrNdBpGMv8")
]

# function call  to render the page in browser using fresh_tomatoes
fresh_tomatoes.open_movies_page(movie_list)
