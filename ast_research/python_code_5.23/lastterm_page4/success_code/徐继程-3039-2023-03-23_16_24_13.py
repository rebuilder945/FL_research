lst=eval(input())
max0=max(lst)
min0=min(lst)
for x in range(len(lst)):
    if max0 in lst:
        lst.remove(max0)
    else:
        break
for x in range(len(lst)):  
    if min0 in lst:
        lst.remove(min0)
    else:
        break
print(lst)


