n=input()
letter,space,digit,others=0,0,0,0
for x in n:
    if x.isalpha():
        letter+=1
    elif x.isspace():
        space+=1
    elif x.isdigit():
        digit+=1
    else:
        others+=1
print(letter,space,digit,others)
