z={}
for i in range(26):
    z[chr(ord("A")+i)]=chr(ord("A")+25-i)
    z[chr(ord("a")+i)]=chr(ord("a")+25-i)
a=input()
c=""
for i in a:
    if "a"<=i<="z" or"A"<=i<="Z":
        c+=z[i]
    else:
        c+=i
print(c)

            

