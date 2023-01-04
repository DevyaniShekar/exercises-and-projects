#fix errors - re-run program
#each time you fix an error add comment in the line here you fixed it indicate what kind of error it was (out of the 3)


print ("Welcome to the error program")        #missing paranthesis - syntax error
print ("\n")                                  #indentation error and missing parenthesis  - syntax error

age_Str == "24"      #indentation error - also strange commentary? - typeerror error - mixing strings with numbers - == had equals equals - variable name
age = int(age_Str)                      #indentation error
print(f"I'm {age} years old.")      #indentation error + typeerror error cannot concatenate int to str + logical error as no f-string
   #indentation error +typeerror unnecesary name variable creation of number

answerYears = age + 3              #indentation error  - typeerror error - cannot add int and string

print (f"The total number of years: {answerYears}")      #missing paranthesis incorrect quotation marks around variable Typeerror error - can't concatenate integer and string
answerMonths = answerYears * 12           #syntax error variable is incorrectly spelt meant answerYears not answer
print (f"In 3 years and 6 months, I'll be {answerMonths + 6} months old")   #missing parenthesis cant concatenate int and str - logical error - displays incorrect value of 324 initially because no calculation to add 6 was made only printed 

#HINT, 330 months is the correct answer