D={}
for i in range(26):
    D[chr(ord("A")+i)]=chr(ord("A")+25-i)#先退至最后再对称往前
    D[chr(ord("a")+i)]=chr(ord("a")+25-i)
p=input()
c=""
for i in p:
    if "a"<=i<="z" or "A"<=i<="Z":
        c+=D[i]
    else:
        c+=i
print(p)
print(c)

