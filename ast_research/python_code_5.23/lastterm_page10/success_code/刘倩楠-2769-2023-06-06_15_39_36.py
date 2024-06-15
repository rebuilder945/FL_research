n=list(input())
print(''.join(n))
for x in list(range(len(n))):
    if n[x].islower():
        s=chr(97+(123-ord(n[x]))-1)
        n[x]=s
    elif n[x].isupper():
        q=chr(65+(91-ord(n[x]))-1)
        n[x]=q
print(''.join(n))
