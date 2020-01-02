from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
#from urllib.request import urlretrieve

print("\nTypical Tuple: ")
user = ('bob','coder')
print(user[0])
print(user[1])


#named Tuple
print("\nNamed Tuple")
User = namedtuple('user', 'name role')

user01 = User(name='Bill', role='Dev')
user02 = User(name='Sandy', role='QA')

print(user01.name, " is a ", user01.role)


user_list = [user01, user02]
for user in user_list:
    print(user.name, " - ", user.role)

#dictionary
print("\ndefault dict examples")
user = {'bob':'coder'}
print(user)


user["bob"]
# user["Julien"] ## Will default to an error ##

print(user.get('bob'))
#print(user.get('julian') is none)


# Create a dictionary
MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Florida='Marlins',
    Cleveland='Indians'
    )


print(MLB_team)

# Another way to create

NBA_team = dict([
    ('Chicago', 'Bulls'),
    ('Boston', 'Celtics'),
    ('Detroit', 'Pistons'),
    ('Orlando', 'Magic')
])

print(type(NBA_team))
print("\n",NBA_team)



# Iteration through key and values of a dictionary via the items method
for key, value in NBA_team.items():
    print(key, "-------", value)

print("\n")

for x in NBA_team.items():
    print(x, "is a --->", type(x))
    
    
# Dictionary keys
print("\n")
print(NBA_team.keys())

for x in NBA_team.keys():
    print(x)

print("\n")
for x in NBA_team.keys():
    print(x, "has the --", NBA_team[x])


# Dicationary values
print("")
print(NBA_team.values())


print("")
for value in NBA_team.values():
    print(value)

print("")
print("Knicks in dictionary: ","Knicks" in NBA_team.values())
print("Magic in dictionary: ", "Magic" in NBA_team.values())

print("")

# Make a list of tuples that will be converted to a dict.
challenges_done = [('mike', 10),('Julian', 7),('Bob', 5),
                   ('mike', 11), ('Julian', 8), ('Bob', 6)]

print(challenges_done)

for x,y in challenges_done:
    print(x, 'is ', y)

# Goal is to convert into a dictionary.
# a regular dictionary will fail.
# uncomment to demonstrate failure.

#challenges = {}
#for name, challenge in challenges_done:
#    challenges[name].append(challenge)

# By using a default dict this goal can be accomplished.
# you need to define what type the values hold.
# in this case the key is the user and the value is a list of challenge numbers.

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)


print(challenges.items())
