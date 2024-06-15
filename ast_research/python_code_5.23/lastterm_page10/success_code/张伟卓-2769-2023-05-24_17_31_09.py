a=" abcdefghijklmnopqrstuvwxyz "
b=" ABCDEFGHIJKLMNOPQRSTUVWXYZ "
w=input()
z=''
for i in list(w):
    if i in a:
        z+=a[26-a.index()+1]
    elif i in b:
        z+=b[26-b.index()+1]
    else:
        z+=i
print(w+"\n"+z)

