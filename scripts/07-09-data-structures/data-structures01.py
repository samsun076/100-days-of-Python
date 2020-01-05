# data structures - https://codechalleng.es/bites/21/
# Bite 21. Query a nested data structure

#DIRECTIONS
# Given the provided cars dictionary:
#  Get all Jeeps
#  Get the first car of every manufacturer.
#  Get all vehicles containing the string Trail in their names (should work for other grep too)
#  Sort the models (values) alphabetically

#More specific directions givin in the  docstrings of functions


# Provided Dictionary
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

# Playing with basic ways of looping through the dictionary
print("---- Iterations Playings -----")
for model in cars:
    print(model)
print("")

for model, car in cars.items():
    print(model, ': ', car)

print("")
for model in cars:
    print(model, cars[model])

print("\n------- Pybites Tasks, functions not included -------")
print('''01: return a comma  + space (', ') separated string of jeep models (original order)''')

jeep_models = cars["Jeep"]
print("\t",', '.join(jeep_models))



print("""\n02: return a list of matching models (original ordering)""")
# For Loop Method.
car_list=[]
for model in cars.values():
    car_list.append(model[0])
print("\tFor Loop method: ",car_list)

# List comprehension method.
print("\tList Comprehension method: ",[model[0] for model in cars.values()])



print("""\n03: return a list of all models containing the case insensitive
'grep' string which defaults to 'trail' for this exercise""")
#print(cars.values())
search_term="trail"
result=[]
for car_list in cars.values():
    for car in car_list:
        if search_term in car.lower():
            #print(car)
            result.append(car)
        #else:
            #print(search_term, "not in ", car)

print("\tFor Loop Result:",result)
print("\tList Comprehension Result:",[car for car_list in cars.values() for car in car_list if search_term in car.lower()])





print("""\n04: return a copy of the cars dict with the car models (values) sorted alphabetically""")
for key, value in sorted(cars.items()):
    print("\t",key, sorted(value))


