# tuple with favorite things
favorite_things = ('Interstellar', 'Imagine', 'To Kill a Mockingbird')
print("Favorite things:", favorite_things)

# Trying to change an element 
try:
    favorite_things[0] = 'Inception'
except TypeError:
    print("Oops! Tuples cannot be changed.")

# Print
print("Length of tuple:", len(favorite_things))
