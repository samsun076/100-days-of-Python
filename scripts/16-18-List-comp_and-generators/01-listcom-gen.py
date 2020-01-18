
# examples from list comp's and generators
# https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/16-18-listcomprehensions-generators/list-comprehensions-generators.ipynb\\



from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests


# Create a list of names and run it
names = 'pybites mike bob julian tim sara guido'.split()
print(names)

# Typical For loop
for name in names:
    print(name.title())


first_half_alpha = string.ascii_lowercase[:13]
print("\n",first_half_alpha)

# typical way to create an empty list, loop through names list
# find names that start with the first half of the alphabet
# and capitalize the name

new_names=[]
for name in names:
    if name[0] in first_half_alpha:
        new_names.append(name.title())
print(new_names)

# now with list comps

new_names2 = [name.title() for name in names if name[0] in first_half_alpha]
print(new_names2)


assert new_names == new_names2


# another example to get common word requests on an excerpt of Harry Potter
resp = requests.get("http://projects.bobbelderbos.com/pcc/harry.txt")

# get all words in excerpt, make them lowercase, and split them up into a list
potter_words_list = resp.text.lower().split()
print(potter_words_list[:5])

# create a CNT variable and print the number of instances of each letter
cnt = Counter(potter_words_list)
print(cnt)
# 5 most common words
print(cnt.most_common(5))

# basic function with list comp to check if stop words or non alpha numeric exist in excerpt
sample_stop_words = "- the to fuck".split()
def stop_word_check(word_list=potter_words_list):
    return[word in word_list for word in sample_stop_words]

#check to see if stop words exists. Returns True or False.
print(stop_word_check())

# clean up non alpha numeric chars and set new variable name.  \W is any non word character.
# '+' is one or more.  So replacing and instances of one or more non word characters with nothing.
new_words = [re.sub(r'\W+', r'', word) for word in potter_words_list]

print(stop_word_check(new_words))
cnt = Counter(new_words)
cnt.most_common(5)


resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
full_stop_words = resp.text.lower().split()
print(full_stop_words[:5])

#traditional for loop
loop_list=[]
for word in new_words:
    if word.strip() and word not in full_stop_words:
        loop_list.append(word)

print(loop_list)

#comprehension list
comp_list = [word for word in new_words if word.strip() and word not in full_stop_words]
print(comp_list)

cnt = Counter(comp_list)
print(cnt.most_common(10))




