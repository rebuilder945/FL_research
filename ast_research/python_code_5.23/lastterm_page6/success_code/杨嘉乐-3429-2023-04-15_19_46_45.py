m=str(input())
alaph=0
space=0
digit=0
other=0
for i in m:
    if i.isspace():
        space+=1
    elif i.isalpha():
        alaph+=1
    elif i.isdigit():
        digit+=1
    else:
        other+=1
print("%d %d %d %d"%(alaph,space,digit,other))

