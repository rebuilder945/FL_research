li=list(eval(input()))
ma=max(a)
mi=min(a)
while ma in li:
    li.pop(ma)
while mi in li:
    li.pop(mi)
print(li)
