a=input()
b=input()
for i in range(len(a)):
    if a[i]==b:
        c=list(a)
        while b in c:
            c.remove(b)
print(*c)
