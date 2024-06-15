a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
z = ""
for i in list(s):
    if i in a:
        z += a[26-a.index(i)]
    elif i in b:
        z += b[26-b.index(i)]
    else:
        z += i
print(s+"\n"+z)            
