D={}
for i in range(26):
    D[chr(ord("A")+i)]=chr(ord("A")+26-i+1)
    D[chr(ord("a")+i)]=chr(ord("a")+26-i+1)
p=input()
c=""
for i in p:
    if "a"<=i<="z" or "A"<=i<="Z":
        c+=D[i]
    else:
        c+=i
print(p)
print(c)


