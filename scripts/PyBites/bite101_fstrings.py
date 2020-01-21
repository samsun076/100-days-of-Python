MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if age <MIN_DRIVING_AGE:
        print(name, "cant drive and is: ", age)
        print(MIN_DRIVING_AGE)
        print()
    else:
        print(name, age, "can drive...")


def allowed_to_drive(name, age):
    """PyBites solutions to the above function"""
    is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
    print(f'{name} {is_allowed} to drive')

def allowed_2_drive(name, age):
    """Another Cheeky example"""
    print(f'{name.title()} is allowed to drive' if age >= MIN_DRIVING_AGE else f'{name} is not allowed to drive')

allowed_driving("leslie", 5)
allowed_driving("parker", 19)

print()

allowed_to_drive("Dave", 5)
allowed_to_drive("Will", 51)

print()

allowed_2_drive("janice", 100)
allowed_2_drive("Flip", 17)