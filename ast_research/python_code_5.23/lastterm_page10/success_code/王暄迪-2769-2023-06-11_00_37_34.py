a="abcedfghijklmnopqrtsuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
w=input()
z=''
for i in list(w):
    if i in a:
        z+=a[26-a.index(i)+1]
    elif i in b:
        z+=b[26-b.index(i)+1]
    else:
        z+=i
print(w+"\n"+z)
