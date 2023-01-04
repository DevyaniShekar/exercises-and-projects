#create a while loop that will display count down from 20 to 0
num = 20

print("Count down from 20 to 0:")     #added these descriptions to seperate the outputted number loops

while num > -1:
    print(num)
    num -= 1

#next create a loop (any) that will display all even numbers between 1 and 20
print("\ndisplay all even numbers between 1 and 20: ") #assuming including 20
for num in range (1,21): 
    if num % 2 == 0:       #for even number modulus 2 will be zero
        print(num)



#create a loop that will produce the folloing output: *\n**\n***\n****\n*****
i = 1 #initialise to 1 not zero
while i < 6:
    print("*" * i)
    i+=1   #increment the count

#compute greatest common divisor of two positive integers
#I looked at multiple examples of how to calculate this
#seems you can do this by importing the math library I saw this solution on website geeks for geeks

import math

num1 = 56    
num2 = 84    
GCD = math.gcd(84, 56)

print(f"The GCD of 56 and 84 is: {GCD}")