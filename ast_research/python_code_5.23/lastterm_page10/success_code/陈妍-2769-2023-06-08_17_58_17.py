D={}
for i in range(26):
    D[chr(ord("A")+1)]=chr(ord("A")+26)
    D[chr(ord("a")+1)]=chr(ord("a")+26)
p=input()
c=""
for i in p:
    if "a"<=i<="z" or "A"<=i<="Z":
        c+=D[i]
print(p)
print(c)


