d={}
for i in range(26):
    d[chr(ord("A")+i)]=chr(ord("A")+25-i)
    d[chr(ord("a")+i)]=chr(ord("a")+25-i)
n=input()
c=""
for i in n:
    if "a"<=i<="z" or "A"<=i<="Z":
        c+=d[i]
    else:
        c+=i
print(n)
print(c)
