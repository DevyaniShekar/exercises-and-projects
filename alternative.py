#program that makes each alternate character an uppercase character and other character a lowercase character
#then make each alternative WORD lower and upper case using split and join functions
#slice strings by specifying a range from one index to another starting index is included end is not
string = input("Please enter a phrase: ") 
letters = len(string)
b = 0
word = []

while b < letters:
    if b % 2 == 0:    
        word.append(string[b].lower())
    else:
        word.append(string[b].upper())
    b = b+1

print(''.join(word))     #I got help to find this solution from stack overflow from MeeshcompBio whoever he his and my mum


#task 2
#string = 
#new_string = string[0:5]
#print(new_string)
#.lower()    .upper()
#.strip()  #removes whitespaces from beginning and end
#.split('')
#"".join(string_list)  


new_string = input("Please enter a string: ")


#split the sentence into words
string_split = new_string.split()   


#empty list to store a split list of words, 

words =""

#make every alternate word capitalised

for i in range(0, len(string_split)): # make every second letter upper

    if i % 2 == 0:
        words = words + " "+ string_split[i].lower() 

    else:
        words = words +" " + string_split[i].upper() 
    

#join the individual characters
alternate_cap = "".join(words)

#print results
print(alternate_cap)