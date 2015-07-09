__author__ = 'davidkavanagh'
import sys
from fresh_tomatoes import open_movies_page

class Movie(object):

    def __init__(self, title, year, director, art_url, youtube_url):
        self.title = title
        self.year = year
        self.poster_image_url = art_url
        self.trailer_youtube_url = youtube_url
        self.director = director

    def __unicode__(self):
        return '{0} [{1}]'.format(self.title, self.year)

if __name__== '__main__':

    # Store movie data in a file. Easier to add or edit than changing code.
    try:
        source_data = open('../data/movies.txt', 'r')
    except IOError:
        sys.stderr.write('../data/movies.txt not accessible. Does the file exist?\n')
        sys.stderr.flush()
        sys.exit(1)

    my_movies = []
    for line in source_data:
        fields = line.rstrip().rsplit('\t') #remove newline character. Split on tabs
        movie_title = fields[0]
        release_year = fields[1]
        movie_director = fields[2]
        movie_art_url = fields[3]
        movie_youtube_url = fields[4]

        my_movies.append(
            Movie(
                movie_title,
                release_year,
                movie_director,
                movie_art_url,
                movie_youtube_url,
            )
        )
    open_movies_page(my_movies)







