#write code to take in a users age and store their age in an integer variable called age
#check if the users age is 18 or older. if user 18 or older print "u are old enough"
#else-if they are over 16 but under 18 print "almost there"
#otherwise print "you're just too young"


#ask user to enter their age and store the input in the variable "age"
age = int(input("Enter your age: "))
#use if control structure so that when age is greater than or equal to 18 phrase - "You are old enough will print"
if age >= 18:
    print("You are old enough!")
#use elif so that else -> if the age is less than 18 AND greater than 16 the phrase "almost there" will print
elif age > 16 and age < 18:
    print("Almost there")
#otherwise, if neither "if" nor "elif" control structure satisfied print "you're just too young"
else:
    print("You're just too young")    
