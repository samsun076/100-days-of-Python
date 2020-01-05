from collections import defaultdict, namedtuple, Counter, deque
import csv


file= 'collections_directors.csv'
Movie = namedtuple('Movie', 'title year score')

directors = defaultdict(list)

with open(file) as f:
    for line in csv.DictReader(f):
        try:
            #printing out test lines
            #print("")
            #print(line)
            #printing out ordereddict
            #for key, value in line.items():
            #    print(key, value)

            director = line['director_name']
            movie = line['movie_title']
            year = int(line['title_year'])
            score = float(line['imdb_score'])
        except ValueError:
            continue

        m = Movie(title=movie, year=year, score=score)
        directors[director].append(m)
        #more printing of test
        #print("")
        #print(m)
        #print(directors)


for x in directors['Quentin Tarantino']:
    print(x)

