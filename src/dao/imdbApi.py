import xmltodict
# import json
from src.handlers.imdbApi import handler


class ImdbApi():

    def __init__(self):

        self.__handler = handler

    def search_movie(self, title, max='10'):

        print('\n\t+ Searching movies with title: {}\n'.format(title))
        result = self.__handler.search_movie(title)
        print(type(result))
        # print(dir(result[0]))

        movies = []

        for movie in result[0:int(max)]:
            my_dict = xmltodict.parse(movie.asXML())
            # json_data = json.dumps(my_dict)
            # print(json_data)
            movies.append(my_dict)
            # title = movie['title']
            # year = movie['year']
            # print(f'{title} - {year}')

        if not movies:
            return 404
        return movies


'''
# # Help?
# print(dir(handler))
# ----------------------------------------
# 1) Search for a title
movies = handler.search_movie('inception')

# print('Searching for "inception":')
# for movie in movies:
#     title = movie['title']
#     year = movie['year']
#     print(f'{title} - {year}')

# Help?
# print(movies[0].keys())


# ----------------------------------------
# 2) List movie info
id = movies[0].getID()
movie = handler.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

print('\nMovie info:')
print(f'{title} - {year}')
print(f'rating: {rating}')

print(f'\nDirectors:')
for director in directors[0:9]:
    print(f'{director}')
print()

# direcStr = ' '.join(map(str, directors))
# print(f'directors: {direcStr}')

print(f'\nCasting:')
for actor in casting[0:9]:
    print(f'{actor}')
print()

# actors = ', '.join(map(str, casting))
# print(f'actors: {actors}')

# Help?
# print(movie.keys())
# ----------------------------------------
# 3) List actor info
# id = casting[0].getID()
# person = handler.get_person(id)
# bio = handler.get_person_biography(id)

# name = person['name']
# birthDate = person['birth date']
# height = person['height']
# trivia = person['trivia']
# titleRefs = bio['titlesRefs']

# print(f'name: {name}')
# print(f'birth date: {birthDate}')
# print(f'height: {height}')
# print(f'trivia: {trivia[0]}')

# titleRefsStr = ', '.join(map(str, titleRefs))
# print(f'bio title refs: {titleRefsStr}')

# Help?
# print(dir(casting[0]))
# print(person.keys())

# Help?
# print(bio.keys())
# print(bio['titlesRefs'].keys())
# ----------------------------------------
# 4) Get top/bottom 10 movies
# top = handler.get_top250_movies()
# bottom = handler.get_bottom100_movies()

# print('Top 10 movies:')
# for movie in top[0:9]:
#     print(movie)
# print()

# print('Bottom 10 movies:')
# for movie in bottom[0:9]:
#     print(movie)
'''
