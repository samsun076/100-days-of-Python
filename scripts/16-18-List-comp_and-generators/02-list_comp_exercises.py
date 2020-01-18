names = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


for name in names:
    print(name.title())
    print(name.upper())
    # Slicing used to do first last.
    # split the names and revers them with ::-1
    # the above step creates the first last names in a list
    # the join command joins them back into a string with a space delimiter
    # title() method adds caps to first letter of each name
    print(' '.join(name.split()[::-1]).title())
    print()

print("\nList Comprhension")
#Now with list comprehensions

print('\n'.join([(name.title()) for name in names]))
print()
print('\n'.join([' '.join(name.split()[::-1]).title() for name in names]))

#Talk Python solution
def reverse_first_last_names(name):
    first, last = name.split()
    # ' '.join([last, first]) # Can userf-strings in python >= 3.6
    return f'{last} {first}'

print("\nTalk Python Solution")
for x in names:
    print(reverse_first_last_names(x))



