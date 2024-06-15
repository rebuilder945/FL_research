a=input()
ma=max(a)
mi=min(a)
while ma in a:
    a.pop(ma)
while mi in a:
    a.pop(mi)
print(a)
