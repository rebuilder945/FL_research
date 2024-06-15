a=input()
b=input()
c=[x for x in a]
for i in range(len(a)):
    if a[i]==b:
        while b in c:
            c.remove(b)
print(str(c))
