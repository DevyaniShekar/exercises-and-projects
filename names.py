#require the user to enter the names of all pupils in a class
#user should be able to enter "stop" to indicate all names have been entered
#print out total number of names the user entered
#save names in a list

print("Enter the names of all the pupils in your class.\n Type 'stop' to indicate that all the names have been entered.")

name_counter = 0 #initialise name counter to zero

while True: 
    names = input("Enter a name: ")
    names = names.lower()

    if names == "stop":
        print(f"There are {name_counter} pupils")

        break
    name_counter += 1  #add one to counter with every student
