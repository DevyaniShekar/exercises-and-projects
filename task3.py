#design a program that determines the award a person competeing in a triathalon will recieve
#ask user for time completed event (swimming, cycling, running) read time in minutes
#add times together, calculate time taken to complete triathalon
#if total time <= 100 qualifies for an award
#display the award the participant will recieve based on the following criteria:
#within qualifying time <= 100 mins = provincial colours
#time <= 105 minutes and > 100 = provincial half colours
#time <= 110 minutes and > 105 = provincial scroll
#more than 10 minutes of qualifying time else = no award

swim = int(input("Please enter how much time, in minutes, the swim was completed in: "))
cycle = int(input("Now enter how much time, in minutes, the cycle was completed in: "))
run = int(input("Finally, enter how much time, in minutes, the run was completed in: "))

total_time = swim + cycle + run

if total_time <= 100:
    print("This participant recieves Provincial Colours, Congrats!")
elif total_time <= 105 and total_time > 100:
    print("This participant recieves Provincial HALF colours, nice")
elif total_time <= 110 and total_time > 105:
    print("This participant recieves a Provincial scroll, cool")
else:
    print("This participant is awarded NOTHING")    
