str_manip = input("Please enter a sentence: ")
print(f"The number of characters in the sentence is: " + str(len(str_manip)))
position = str_manip[-1]
print(str_manip.replace(position, "@"))
print(str_manip[-1] + str_manip[-2] + str_manip[-3])
print(str_manip[0:3] + str_manip[-2] + str_manip[-1])