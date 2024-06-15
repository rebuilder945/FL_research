a=input()
n=len(a)
a=a.split()
x=''
for i in a:
    x=x+i
k=n-len(x)
y=s=q=0
m='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
n='1234567890'
for i in x:
    if i in m:
        y=y+1
    elif i in n:
        s=s+1
    else:
        q=q+1
print(y,k,s,q)
