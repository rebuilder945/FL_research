li=list(eval(input()))
ma=max(li)
mi=min(li)
while ma in li:
    li.pop(ma)
while mi in li:
    li.pop(mi)
print(li)
