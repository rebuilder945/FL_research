a=input()
b=list(a)
c='abcdefghijklmnopqrstuvwxyz'
d='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
e=''
for i in b:
    if i in list(c):
        e+=c[26-c.index(i)-1]
    elif i in list(d):
        e+=d[26-d.index(i)-1]
    else:
        e+=i
print(a)
print(e)

