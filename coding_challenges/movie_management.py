#Define Movie class having attributes of a movie: title and director and a _is_available parameter to track the availability of the book
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self._is_rented_out = []

    def rent_movie(self):
        if not self._is_rented_out:
            self._is_rented_out = True
            return True
        return False
    
    def return_movie(self):
        if self._is_rented_out:
            self._is_rented_out = False
            return False
        return False
    
    def movie_available(self):
        return not self._is_rented_out

#Define Library class to store instances of books and display available books    
class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def list_all_movies(self):
        for movie in self.movies:
            print(f"{movie.title} by {movie.director}")

    def list_available_movies(self):
        for movie in self.movies:
            if movie.movie_available():
                print(f"{movie.title} by {movie.director}")

    def rent_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                if movie.movie_available():
                    print(f"Movie '{title}' is rented out.")
                    return movie.rent_movie()
                else:
                    print(f"Movie '{title}' is already rented out.")
                    return False
        print(f"Movie '{title}' is not found in the library.")
        return False
    
    def return_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                if not movie.movie_available():
                    print(f"Movie '{title}' returned.")
                    return movie.return_movie()
                else:
                    print(f"Movie '{title}' was not rented out.")
                    return False
        print(f"Movie '{title}' is not found in the library.")
        return False
  
    def list_available_movies(self):
        for movie in self.movies:
            if movie.movie_available():
                print(f"{movie.title} by {movie.director}")