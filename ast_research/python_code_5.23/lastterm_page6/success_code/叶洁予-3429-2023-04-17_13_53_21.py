s=input()
letters,spaces,digits,others=0,0,0,0
for c in s :
    if c.isalpha():
        letters +=1
    elif c.isspace():
        spaces +=1
    elif c.isdigit():
        digits +=1
    else:
        others +=1
    print(letters,spaces,digits,others)

