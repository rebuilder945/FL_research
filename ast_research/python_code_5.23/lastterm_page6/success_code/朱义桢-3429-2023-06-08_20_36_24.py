a=input()
b=[0,0,0,0]
for x in a[:]:
    if x.isdigit():
        b[2]+=1
    elif x.isalpha():
        b[0]+=1
    elif x==" ":
        b[1]+=1
    else:
        b[3]+=1
for x in b:
    print(x,end=" ")
