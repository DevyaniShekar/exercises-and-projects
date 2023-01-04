#use for loops in order to display the times tables for any number
#print from start (1) to end (12)

num = int(input("Please enter the number you would like the multiplication table of: "))
print(f"The multiplication table of {num} is: ")

#print from 1-12th position
for count in range(1,13):    #in order to display 12th ask for range up to 13th  
    print(num, 'x', count, '=', num*count )