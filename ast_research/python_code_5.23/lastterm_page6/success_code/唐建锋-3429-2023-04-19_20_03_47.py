n=input()
myletters=0
myspaces=0
mynums=0
others=0
for i in n:
    if i.isalpha():
        myletters+=1
    elif i.isspace():
        myspaces+=1
    elif i.isdigit():
        mynums+=1
    else:
        others+=1
print(myletters,myspaces,mynums,others)
