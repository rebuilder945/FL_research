a=" abcdefghijklmnopqrstuvwxyz "
b=" ABCDEFGHIJKLMNOPQRSTUVWXYZ "
w=input()
c=[]
for i in list(w):
    if i in a:
        d=a[26-a.index(i)+1]
        c.append(d)
    elif i in b:
        d=a[26-a.index(i)+1]
        c.append(d)
print(w)
print(c)

