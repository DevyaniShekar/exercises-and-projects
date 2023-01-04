#write a program that always asks a user to enter a number
#when the user enters -1 the program should stop requesting the user to enter a number
#the program must then calculate the average of the numbers entered, excluding the -1
#make use of the while loop repitition structure

print("enter a number, enter -1 to stop the loop ")
number_input = 0 #counter += 1
all_inputs = []

while True:
    number_input = int(input("Enter number: "))
    if number_input == -1:
        break
        
    else:
        all_inputs.append(number_input)
print(sum(all_inputs) / len(all_inputs))       
