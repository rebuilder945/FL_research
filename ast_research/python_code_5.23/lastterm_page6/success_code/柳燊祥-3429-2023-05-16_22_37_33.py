lst1=list(input())
x=0
j=0
k=0
p=0
for i in lst1:
    if (ord(i)>=65 and ord(i)<=90)or(ord(i)>=97 and ord(i)<=122):
        x+=1
    elif ord(i)>=48 and ord(i)<=57:
        j+=1
    elif i==' ':
        k+=1
    else:
        p+=1
print(x,k,j,p,end="")
