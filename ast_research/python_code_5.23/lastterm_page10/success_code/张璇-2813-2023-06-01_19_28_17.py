a=input()
b=input()
c=list(a)
for x in range(len(c)):
    if c[x]==b:
        c.remove(c[x])
d=''.join(c)
print(d)

