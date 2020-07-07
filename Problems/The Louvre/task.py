class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def info(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.')


user_title = input()
user_artist = input()
user_year = input()
my_painting = Painting(user_title, user_artist, user_year)
my_painting.info()
