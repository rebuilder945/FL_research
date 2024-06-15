a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=input()
t=''
for i in s:
    if i in a:
        t+=a[26-a.index(i)-1]
    elif i in b:
        t+=a[26-b.index(i)-1]
    else:
        t+=i
print(s)
print(t)
