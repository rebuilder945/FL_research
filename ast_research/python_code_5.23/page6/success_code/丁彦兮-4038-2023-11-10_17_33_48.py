a=input()
m=0
n=0
b=0
d=0
for i in a:

    if a.isalpha():
        m+=1
    elif a.isspace():
         n+=1
    elif a.isdigit():
         b+=1
    else:
         d+=1

print(m,n,b,d,end="")
