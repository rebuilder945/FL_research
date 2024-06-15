s=input()
s1=list(s)
a1=0
a2=0
a3=0
a4=0
for i in s1:
    if i in "0123456789":
        a3+=1
    elif i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a1+=1
    elif i==" ":
        a2+=1
    else:
        a4+=1
print(a1," ",a2," ",a3," ",a4)
