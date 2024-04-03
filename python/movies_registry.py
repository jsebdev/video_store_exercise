from movie import ChildrenMovie, RegularMovie, MovieType

class MovieRegistry():
    movie_classes = {
        MovieType.REGULAR: RegularMovie,
        MovieType.CHILDREN: ChildrenMovie
    }

    def __init__(self):
        self.movies = {}

    def add_movie(self, movieTitle, movieType):
        movieClass = self.movie_classes[movieType]
        self.movies[movieTitle] = movieClass(movieTitle)
    
    def get_movie(self, movieTitle):
        return self.movies[movieTitle]
