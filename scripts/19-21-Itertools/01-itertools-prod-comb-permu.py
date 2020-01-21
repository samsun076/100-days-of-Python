from itertools import product, permutations, combinations

# short for a cartesian product
# every possible combination of numbers

# how many different combinatation of the below letters can you get.
# itertools product can calculate that for you

for letter in product('python', repeat=1):
    print(letter)



# combinations allows you to get the possible combos or a certain iterable.
# order of combinations is not in order.
# if order matters, user permutations

friends = "mike, bob, julian".split()

print('Combinations: ', list(combinations(friends,2)))
print('Permutations: ', list(permutations(friends, 2)))
print('Permutations: ', list(permutations(friends, 3)))

