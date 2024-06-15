s=input()
x=len(s)
t="".join(s.split())
y=len(t)
b=x-y
a=c=d=0
m="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
n="1234567890"
for i in t:
    if i in m:
        a+=1
    elif i in n:
        c+=1
    else:
        d+=1
print(a,b,c,d)

