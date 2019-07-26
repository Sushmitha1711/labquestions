word=input("enter the word:")
if word.endswith("y"):
    word=word[:-1]+"ies"
print(word)