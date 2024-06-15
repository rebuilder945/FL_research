a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
w = input()
z = ""
for i in list(w):
    if i in a:
        z+=a[25-a.index(i)]
    elif i in b:
        z+=b[25-b.index(i)]
    else:
        z+=i
print(w+"\n"+z)

