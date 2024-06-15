s=input()
z=''
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in list(s):
    if i in a:
        z+=a[26-a.count(i)+1]
    elif i in b:
        z+=b[26-b.count(i)+1]
    else:
        z+=i
print(s+"\n"+z)
