n=input()
lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(n)
for i in range(len(n)):
    if n[i].isupper():
        s=lst.index(n[i])
        n[i]=lst[26-s]
    if n[i].islower():
        s=lst.index(n[i].upper())
        t=lst[26-s]
        n[i]=t.lower()
print(n)

