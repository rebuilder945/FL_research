a=input()
b=input()
s=''
c=[x for x in a]
for i in range(len(a)):
    if a[i]==b:
        while b in c:
            c.remove(b)
for y in c:
    s+=str(y)
print(s)
