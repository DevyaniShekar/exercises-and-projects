#write a program to input a year and a number of years
#use for loops to determine and display which of those years are leap years

print("Enter a year to see if it is a leap year and then enter the number of years after that you want to check for leap years")

start_year = int(input("What year do you want to start with: "))
num_years = int(input("How many years do you want to check: "))

for num in range(start_year, (start_year + num_years)): 
    if ((num % 4) == 0):       #if a year is a leap year it will be a multiple of 4 so modulus of 4 should be zero
         print(f"{num} is a leap year")
    else:
         print(f"{num} is not a leap year")
