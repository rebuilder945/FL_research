li=list(eval(input()))
ma=max(li)
mi=min(li)
while ma in li:
    li.remove(ma)
while mi in li:
    li.remove(mi)
print(li)
