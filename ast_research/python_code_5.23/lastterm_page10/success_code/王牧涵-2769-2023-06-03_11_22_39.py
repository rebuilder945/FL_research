a=" abcdefghijklmnopqrstuvwxyz "
b=" ABCDEFGHIJKLMNOPQRSTUVWXYZ "

w=input()
z=''
for x in list(w):
    if x in a:
        z+=a[26-a.index(x)+1]
    elif x in b:
        z+=b[26-b.index(x)+1]
    else:
        z+=x
print(w+"\n"+z)
