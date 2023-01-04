num1 = 8
num2 = 4
num3 = 9

#compare 1 and 2 display the larger value
if num1 > num2:
    largest = num1
elif num2 > num1:
    largest = num2
print(f"the largest number between num1 and num2 is: {largest}")

# even if the modulus 2 is zero 
if num1%2 == 0:
    print("num1 is even")
if num1%2 != 0:
    print("num1 is odd!")    

#a condiitonal to see which is the largest of them all
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print(f"The largest number is {largest}")
