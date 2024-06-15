n=input().split()
lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print("".join(n))
for i in range(len(n)):
    if n[i].isupper():
        s=lst.index(n[i])
        n[i]=lst[25-s]
    if n[i].islower():
        s=lst.index(n[i].upper())
        t=lst[25-s]
        n[i]=t.lower()
print("".join(n))

