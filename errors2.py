# look at the error messages and find and fix the errors.

animal = "Lion"     #syntax error - no quotation marks around to signify a string
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth")      #no parenthesis syntax error - logical error - no f string but code runs, printing variable names and brackets instead of values

print(full_spec)    #parenthesis missing - syntax error 