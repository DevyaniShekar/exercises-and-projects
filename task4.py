#ask user to input a number
#determine if the number is:
#divisible by 2 and 5 - if
#divisible by 2 or 5 - elif
#not divisible by 2 or 5 - else
#use modulus

number = int(input("Please enter a number: "))
if number%2 == 0 and number%5 == 0:
    print("this number is divisible by 2 and 5")
elif number%2 == 0 or number%5 == 0:
    print("this number is divisible by 2 or 5")
else:
    print("this number is not divisible by 2 or 5, TRY AGAIN :)")      