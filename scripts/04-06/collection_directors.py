from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
#from urllib.request import urlretrieve


# Following along desconstructing script from 
# https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/04-06-collections/collections.ipynb
# next steps are to add a function to the below code.

file= 'collections_directors.csv'

#Define a named tuple
Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=file):
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors

directors = get_movies_by_director()

print("\n---------------")
for listing in directors['Steven Spielberg']:
    print(listing)



print("\n---------------")
print("Getting 10 most common directors and their movies in dataset")
# using the counter method from collections
cnt = Counter()
for director, movies in directors.items():
    cnt[director ] += len(movies)

for result in cnt.most_common(10):
    print(result)


