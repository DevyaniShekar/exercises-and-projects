#Write a program called seperation.py that inputs a sentence and then displays each word of the sentence
# on
# a
# separate 
# line
sentence = input("Enter a sentence:")
for item in sentence.split(" "):
    print(item)