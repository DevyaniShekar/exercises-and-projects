#write a code that displays a logical error
#when your code does what you told it to but not what you want it to
#Don't do what you're told!
#not v creative was short on time just an incorrect indentation on the final line meaning error message doesnt play and doesnt loop if niether investment nor bond entered


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



