#create a program that calculates a person's BMI
#Ask the user to enter their weight in kg and their height in m
# Use the formula BMI = (weight in kg)/((height in m)*(height in m)) to calculate the user's BMI
#if BMI >= 30 print the BMI and that they are obese
#if BMI >= 25 but less than 30 print their BMI and that they are overweight
#if BMI >=18.5 but less than 25 print their BMI and that they are a healthy weight
#if BMI < 18.5 print the BMI and that they are underweight

#ask user to input an integer assign the input to the variable "weight" save input using int()
weight = int(input("Please enter your weight in kg: "))
#ask user to input height in m assign input to variable height save input as a float()
height = float(input("Please enter your height in m: "))
#define variable BMI as = variable weight divided by variable float(height * height)
BMI = weight/float(height*height)

#if BMI is larger than or equal to 30, print bmi and that they are obese
if BMI >= 30:
   print(f"BMI:{BMI}-> You are obese")

#if BMI is between 25 to 29, print bmi and that they are overweight   
if BMI >= 25 and BMI < 30:
   print(f"BMI:{BMI}-> You are overweight")

#if BMI is >= 18.5 but less than 25 print their BMI and that they are a healthy weight
if BMI>=18.5 and BMI<25:
    print(f"BMI:{BMI}-> You are normal")

#if BMI < 18.5 print BMI and that they are underweight
if BMI < 18.5:
    print(f"BMI:{BMI}-> You are underweight")

