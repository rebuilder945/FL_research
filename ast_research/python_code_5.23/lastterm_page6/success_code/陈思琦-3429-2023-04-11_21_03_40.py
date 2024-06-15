s=input()
letter=0
space=0
digit=0
other=0
for i in s:
    if i.isalpha():
        letter+=1
    if i.isspace():
        space+=1
    if i.isdigit():
        digit+=1
    if i.isother():
        other+=1
print(letter,space,digit,other)
