#write a program using while loop that asks the user to enter a number
#program should print out all the even numbers from 1 up to (and possibly including) the number inputed
input_num = 1
while (input_num != -1):
    input_num = int(input("please enter a number, type -1 to stop: "))
    counter = 1 
    while counter < input_num:
        counter += 1
        if ((counter % 2) == 0):
            print(counter)
        





