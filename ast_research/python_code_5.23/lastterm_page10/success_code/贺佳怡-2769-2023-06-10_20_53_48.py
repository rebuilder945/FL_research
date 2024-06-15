a=" abcdefghijklmnopqrstuvwxyz "
b=" ABCDEFGHIJKLMNOPQRSTUVWXYZ "
w=input()
c=[]
for i in list(w):
    if i in a:
        c.append(a[26-a.index(i)+1])
    elif i in b:
        c.append(a[26-a.index(i)+1])
print(w)
print(c)

