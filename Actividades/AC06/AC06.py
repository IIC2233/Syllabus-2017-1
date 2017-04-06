from datetime import datetime as dt


def set_id():
    pass


class Cast:
    def __init__(self, movie_title, name, character):
        self.name = name
        self.movie = movie_title
        self.character = character


class Movie:
    get_id = set_id()

    def __init__(self, title, rating, release, *args):
        self.id = next(Movie.get_id)
        self.title = title
        self.rating = float(rating)
        self.release = dt.strptime(release, '%Y-%m-%d')  # 2015-03-04
        self.genres = []


if __name__ == "__main__":
    with open('movies.txt', 'r') as f:
        pass
    with open('cast.txt', 'r') as f:
        pass
