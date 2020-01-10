# COPIED FILE TO PLAY with PYTEST


# data structures - https://codechalleng.es/bites/21/
# Bite 21. Query a nested data structure

#DIRECTIONS
# Given the provided cars dictionary:
#  Get all Jeeps
#  Get the first car of every manufacturer.
#  Get all vehicles containing the string Trail in their names (should work for other grep too)
#  Sort the models (values) alphabetically

#More specific directions givin in the  docstrings of functions

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeep_models = cars["Jeep"]
    jeeps = ', '.join(jeep_models)
    return jeeps

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = [model[0] for model in cars.values()]
    return first_model


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    search_term=grep
    models=sorted([car for car_list in cars.values() for car in car_list if search_term.lower() in car.lower()])
    return models


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    new_sorted_dict={}
    for key, value in cars.items():
        new_sorted_dict[key]=sorted(value)
    return new_sorted_dict


print(get_all_jeeps(cars))
print(get_first_model_each_manufacturer())
print(get_all_matching_models(grep='CO'))
print(sort_car_models())
