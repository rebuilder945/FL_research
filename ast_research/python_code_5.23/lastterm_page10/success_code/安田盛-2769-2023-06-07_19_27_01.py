s=input()
d={}
for i in range(26):
    d[chr(ord("A")+i)]=chr(ord("A")+25-i)
    d[chr(ord("a")+i)]=chr(ord("a")+25-i)
# print(d)
c=""
for i in s:
    if i in d:
        c+=d[i]
    else:
        c+=i
print(s)
print(c)
