# 100 Pays of python code - Day 09
# Playing with lists and Dicts
# https://codechalleng.es/bites/89/

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'

#######################
# get_every_nth_state #
#######################

'''Return a list with every nth item (default argument n=10, so every
10th item) of the states list above (remember: lists keep order)'''

print("01: Basic for loop not using functions")
counter = 0
for state in states:
    counter += 1
    if counter % 10 == 0:
        print("\t",counter, state)

print("\nUsing Functions")
def get_every_nth_state(states=states, n=10):
    counter = 0
    state_list = []
    for state in states:
        counter += 1
        if counter % n == 0:
            #print(counter,state)
            state_list.append(state)
    return state_list


print(get_every_nth_state(n=10))
print(get_every_nth_state(n=5))
###########################
# Get state Abbreviations #
###########################

"""Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
print("\n02: every nth state" )
print("Basic loop looking for abbrev")
my_state = 'Alabama'
if my_state in us_state_abbrev.keys():
    print(us_state_abbrev[my_state])
else:
    print(NOT_FOUND)

print("\nLoop above in a function")
def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    if state_name in us_state_abbrev.keys():
        return us_state_abbrev[state_name]
    else:
        return NOT_FOUND

print(get_state_abbrev(state_name="Pennsylvania"))
print(get_state_abbrev(state_name="Pennsylvaia"))

#####################
# Get longest State #
#####################
"""Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
print("#03: State with the longest string.")
# for the list
print("\nBasic non function ")
print(list(sorted(states, key=len))[-1])

# for the dictionary
print(list(sorted(us_state_abbrev, key=len))[-1])

def test_get_longest_state(data):
    return list(sorted(data, key=len))[-1]

print(test_get_longest_state(states))
print(test_get_longest_state(us_state_abbrev))

#########################################
# Combine State names and abbreviations #
#########################################

"""Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list. The resulting list
       has both sorted, so:
       ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
       (see also test_combine_state_names_and_abbreviations)"""

print("\n04: first and last 10")
#print(sorted(states)[-10:])
list1 = [x for x in sorted(states)[-10:]]
list2 = list(us_state_abbrev.values())[:10]
print(list2 + list1)

print("\nWith Functions:")
def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states):
    list1 = sorted(list(us_state_abbrev.values())[:10])
    list2 = sorted(states)[-10:]
    return list1 + list2
print(combine_state_names_and_abbreviations())