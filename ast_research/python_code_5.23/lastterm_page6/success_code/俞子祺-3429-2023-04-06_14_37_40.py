letter=0
space=0
num=0
other=0
ls=input()
for i in ls:
    if i.isalpha():
        letter +=1
    elif i.isspace():
        space +=1
    elif i.isdight():
        num += 1
    else:
        other += 1
print(letter,space,num,other)
