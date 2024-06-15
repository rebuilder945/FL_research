a=input()
a1=0
a2=0
a3=0
a4=0
for i in a:
    if i.isalpha():
        a1+=1
    elif i.isspace():
        a2+=1
    elif i.isdigit():
        a3+=1
    else:
        a4+=1
print(a1,a2,a3,a4,end=" ")
