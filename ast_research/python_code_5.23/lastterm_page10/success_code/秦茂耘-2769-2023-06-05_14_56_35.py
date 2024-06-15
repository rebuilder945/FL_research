a='abcdefghijklmnopqrstuvwxyz'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
w=input()
z=''
for i in list(w):
    if i in a:
        z+=a[26-a.index(i)]
    elif i in b:
        z+=b[26-b.index(i)]
    else:
        z+=i
print(w+'\n'+z)

