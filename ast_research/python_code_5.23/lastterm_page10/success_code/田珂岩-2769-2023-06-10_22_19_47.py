a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
z = ""
for i in list(s):
    if i in a:
        z += a[26 - a.index(i) - 1]
    elif i in b:
        z += b[26 - b.index(i) - 1]
    else:
        z += i
print(s+"\n"+z)            
