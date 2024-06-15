n=str(input())
for x in list(range(len(n))):
    if n[x].islower():
        p=n[x]
        s=chr(97+(123-ord(n[x]))-1)
        m=n.replace(p,s)
        n=m
    elif n[x].isupper():
        p=n[x]
        q=chr(65+(91-ord(n[x]))-1)
        m=n.replace(p,q)
        n=m
print(n)
print(m)
