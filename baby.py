#this program will be used to test if the user is 18 or older and allowed entry into a party
#ask the user to enter the year they were born and calculate if they are 18 or older
#if they are 18 or older, then display a message saying "congrats you are old enough."
birth_year = int(input("Enter your birth year: "))
if birth_year < 2004:
    print("Congrats you are old enough")