s=input()
z=''
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in list(s):
    if i in a:
        z+=a[27-a.index(i)+1]
    elif i in b:
        z+=b[27-b.index(i)+1]
    else:
        z+=i
print(s+"\n"+z)
