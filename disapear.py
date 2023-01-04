#Write a Python program called disappear.py that strips a set of characters from a string.
#Ask the user to input a string and then ask the user which characters they would like to make disappear.
phrase = input("Enter a string: ")
print(phrase)

characters = input("Enter the characters you would like to make disappear: ")
print(characters)

print(phrase.replace(characters," "))
