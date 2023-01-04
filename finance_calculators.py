import math
#user should be able to choose which calculation they want to do
#user should first get the choice between investment or bond 
#below print a definition of what the resulting calculation would mean 
#investment - to calculate the amount of interest you'll earn on your investment
#bond - to calculate the amount you'll have to pay on a home loan"
#Different capitalisation should be ignored

# When investment is selected ask user to input:
# - amount of money they are depositing
# - the percentage interest rate (entered without the %)
# - the number of years they plan on investing
# - finally ask user to input if they want "simple" or "compound" interest
# store this in a variable "interest"
# output the corresponding amount
# formulae: simple interest = A = P*(1+r*t)
# compund interest = A = P* math.pow((1+r),t)
# where 'A' = total amount after interest
# 'r' = interest entered divided by 100 --> so percentage converted to decimal
# 'P' = amount the user deposits 
# 't' = number of years the money is invested
#print out result

# When Bond selected ask user to input:
# - the present value of the house
# - the interest rate
# the number of months they plan to take to repay the bond 

#  Bond repayment formulae - repayment each month = x = (i.P)/(1-(1+i)^(-n)))
# P = present value of house 
# i = monthly interest rate --> divide annaul interest rate by 12 
#  is the number of months to pay the bond
#calculate and display money to repay each month

invalid_investment_type = True
while invalid_investment_type:

    str = input("\nChoose either 'investment' or 'bond' from the menu below to proceed: \n \n investment - to calculate the amount of interest you'll earn on your investment loan\n Bond -  calculate the amount you'll have to pay on a home loan \n")  #put a \n break at the beginning purely for aesthetic purposes so it wasn't touching the header
    str = str.lower()  #convert the input to lower using .lower()

    if str == "investment":       #compare the input to strings "investment" or "bond"
        invalid_investment_type = False
        deposit = int(input("Please enter the amount of money you would like to deposit: "))
        percentage_int_rate = int(input("Please enter the percentage interest rate: "))   #assuming/hoping the user will know not to enter a percentage symbol
        years = int(input("please enter the number of years you plan on investing: "))
        int_rate = percentage_int_rate/100

        invalid_interest_type = True
        while invalid_interest_type :
            interest = input("Choose either to have 'simple' or 'compound' interest: ")

            if interest == "simple":
                total_interest = deposit*(1+int_rate*years)
                print(f"The amount you will recieve after {years} is: {total_interest}")  #output the amount that they will get back after the given period at the specified interest rate
                invalid_interest_type = False
            
            
            elif interest == "compound":
                total_interest = deposit* math.pow((1+int_rate),years) #formulae = A = P* math.pow((1+r),t)
                print(f"The amount you will recieve after {years} is: {total_interest}")
                invalid_interest_type = False

            else:
                print("Error: Please only enter one of 'simple' or 'compound' no other input valid")    
        


    elif str == "bond":
        invalid_investment_type = False
        p_value = int(input("Please enter the present value of the bond: "))
        percentage_int_rate = int(input("Please enter the percentage interest rate: "))
        num_months = int(input("Please input the number of months you plan to take to repay the bond: "))
        int_rate = percentage_int_rate/100
        repay_months = (int_rate*p_value)/(1-(1+int_rate)**(-num_months))
        print(f"the amount you must repay each month is {repay_months}")        #  Bond repayment formulae - repayment each month = x = (i.P)/(1-(1+i)^(-n)))
        

    else:
        print("Error: Please only enter one of 'investment' or 'bond' no other input valid")   #if the input does not match up exactly output the error message



